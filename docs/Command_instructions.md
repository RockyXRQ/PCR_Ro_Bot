# PCR_Ro_BOT 指令介绍

## 1. 指令使用流程图

![PCR_Bot_Command_Flow](https://raw.githubusercontent.com/RockyXRQ/PCR_Ro_Bot/master/assets/PCR_Bot_Command_Flow.png?token=AIKEPB3UNCUVFPS6TMLN4YK6YZD4G)

## 2. 指令介绍

1. atk_apply

   - 别名：出刀，申请出刀，出刀申请

   - 输入格式：atk_apply(或别名) [出刀阵容] 

     ​				  PS:出刀阵容要求不存在名称重复且各角色名字以空格隔开角色名。

2. atk_finish

   - 别名：完成，出刀完成，完成出刀，出刀完毕
   - 输入格式：atk_finish(或别名) [出刀总伤害]

3. on_tree

   - 别名：挂树，已挂树，申请挂树，会长！我挂树了！
   - 输入格式：on_tree(或别名)

4. save_tree

   - 别名：救树，申请救树，别慌！我来也！
   - 输入格式：save_tree(或别名) [出刀总伤害]
   
5. get_list

   - 别名：查看，查看情况，获取情况
   - 输入格式：get_list(或别名)
   
6. act_apply

   - 别名：代理，变身，代刀
   - 输入格式：act_apply(或别名) [所代理会员昵称]

7. act_cancel

   - 别名：还原，取消代理，取消代刀
   - 输入格式：act_cancel(或别名)

> 指令使用注意事项：
>
> 1. 使用指令前请艾特机器人，PS：复制别人对机器人的艾特是无效的。
> 2. 任何带有参数的指令，在使用时，参数和指令之间须有一空格
> 3. 若使用了某一需要参数的指令，却没有给出参数，此时Bot会自行向你索取参数，此时用户无需艾特机器人，直接发送参数即可。
> 4. 任何指令不可以中途结束，如果机器人在向你索取参数，请先上传好参数，再执行下一指令。