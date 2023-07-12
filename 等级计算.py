# 获取用户输入
current_level = int(input("请输入当前开拓等级："))
current_exp = int(input("请输入当前经验："))
target_level = int(input("请输入目标开拓等级："))
purchase_times = int(input("请输入每天购买几次体力："))

# 每个等级对应的经验列表，索引为开拓等级，值为对应的经验值
exp_per_level = [0,450,500,550,610,670,720,780,840,900,960,1020,1070,1130,1190,1250,1310,1370,1430,1500,1600,1710,1830,1950,2080,2210,2350,2480,2620,2750,2850,2960,3080,3200,3330,3460,3600,3730,3870,4000,4140,4280,4430,4570,4710,4860,5000,5150,5300,5440,5700,6150,6630,7130,7640,8170,8700,9230,9780,10330,20300,21780,23350,24970,26630,65070,68810,72490,76120,79710]
# 计算目标等级所需的总经验
target_exp = sum(exp_per_level[current_level:target_level])

# 计算距离目标等级还需的经验
remaining_exp = target_exp - current_exp

# 每天自然恢复的体力和日常活跃获取的经验
natural_recovery_exp = 240 // 10 * 50
daily_active_exp = {
    0: 1000, 1: 1150, 2: 1300, 3: 1450, 4: 1600, 5: 1750, 6: 1900
}

# 计算每天可获取的经验
if current_level < 65:
    daily_exp = natural_recovery_exp + daily_active_exp.get((current_level-10) // 10, 0)
else:
    daily_exp = natural_recovery_exp + 1900

#每天购买体力所获经验
purchase_exp = purchase_times * 300

#升级所获经验
up_level_exp = (target_level - current_level - 1) * 300

# 计算需要的天数
required_days = (remaining_exp - up_level_exp) // (daily_exp + purchase_exp)
if remaining_exp % daily_exp != 0:
    required_days += 1

# 输出结果
print(f"达到目标等级所需经验：{remaining_exp}")
print("达到目标开拓等级所需的时间为:", required_days, "天")
