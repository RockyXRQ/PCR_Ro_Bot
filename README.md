# PCR_BOT使用说明

## 命令说明
- 申请出刀（atk_apply，出刀申请，出刀）

  - 申请出刀 [阵容名单] PS：名称用空格隔开。

  - 展示当前在攻打boss名称及剩余血量。

    

- 完成（atk_finish，出刀完成，完成出刀，出刀完毕）

  - ！！无论你之前是挂树了，正常攻打，还是救树，最后打完了全部都要使用 完成命令！！

  - 完成  [伤害数值]。

  - 若击杀则当前攻打boss名称自动顺位，血量刷满。

  - 集成了 “下树”、“强制下树”、“救树成功”、“救树失败”（你只管 ’完成‘，剩下的交给程序判断）。

    

- 挂树 （on_tree，已挂树，申请挂树，会长！我挂树了！）

  - 挂树。

  - 昵称加入至挂树列表末端。

    

- 救树 （save_tree，申请救树，别慌！我来也！）

  - 救树 [阵容名单]。

  - 返回当前挂树人员列表，以及救树人员列表。

    

- 查看（get_list，查看情况，获取情况）

  - 查看。
  - 获取当前的攻打名单，挂树名单，和救树名单。