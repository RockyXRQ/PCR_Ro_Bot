from nonebot import on_command, CommandSession

from .commit_atk_damage import commit_atk_damage


@on_command('atk_finish', aliases=('完成', '出刀完成', '完成出刀', '出刀完毕'))
async def atk_finish(session: CommandSession):
    damage = session.get('damage', prompt='请输入您的原始伤害（不是分数）：')

    # 伤害数据是否成功上传
    isDamageAppend = await commit_atk_damage(session.event.sender, damage)

    if isDamageAppend:
        await session.send('出刀数据上传完成！\n您本次的出刀伤害为：\n'+str(damage))
    else:
        await session.send('出刀完成失败，原因可能如下：\n1.您未申请出刀，请先申请出刀再进行出刀数据上传。PS:使用命令【出刀】\
        \n2.当前有人救树，请等待救树完成后再进行【完成】命令。\n3.您输入的伤害小于0\nPS:使用命令【查看】获取救树名单')


@atk_finish.args_parser
async def _(session: CommandSession):
    arg = session.current_arg_text.strip()

    if session.is_first_run:

        if arg:
            session.state['damage'] = arg
        return

    if (not arg):
        session.pause('填写的伤害为空请重新填写！')

    # 若当前正在询问更多信息，且新输入的信息有效，则放入会话状态
    session.state[session.current_key] = arg
