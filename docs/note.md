# item.json
name:中文名
id：物品id
iconPath：图片路径
description:描述
type:物品类型{'LOGISTICS', 'PRODUCTION', 'DEFENSE', 'TURRET', 'MATERIAL', 'PRODUCT', 'RESOURCE', 'DARKFOG', 'COMPONENT', 'MATRIX'}

# reciped.json 
items：原料（参考``item``）
itemsCounts：数量
results：产物（参考``item``）
resultCounts：数量
timeSpend：时间（秒*60）（生产60个需要多少秒）
type：制造方式{'PARTICLE', 'CHEMICAL', 'ASSEMBLE', 'SMELT', 'FRACTIONATE', 'RESEARCH', 'REFINE'}
