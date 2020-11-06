# Created by bkex at 2020/9/14
# language: zh-CN

功能:活期宝转入
  场景大纲:进入活期宝页面-选择已有的币种-点击转入--检验转入是否成功,数量是否正确
      当查询币种<coinType>可用余额
      假如选择<coinType>转入<amount>
      那么币种<coinType>可用余额减少<amount>
    例子: translate_in
      |coinType|amount|
      |USDT|100|
