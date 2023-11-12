import owtime
import datetime

"""
利用owtime获取异世界时间
截止到构建版本时，owtime目前的版本为5.2.2.3
Tips:
以下都是调用owtime的毫秒回复
任何异界时间在Python中实现都需要创建对象
"""


# 创建对象
owtime.owtimes.OWTime(3047, 1, 1, 1, 1, 1, 1)
owtime.owct.OWCT(1, 1, 1, 1)
owtime.owcl.OWCL(3047, 1, 1)

# 获取owts时间(秒级)
get_owts_time = owtime.owts.OWMTS.now()

# 反推owts时间
backstep_owts_time = owtime.owts.OWMTS.from_owts_obj(owtime.owts.OWTS(owtime.owtimes.OWTime.now()))

# 获取owct时间
get_owct_time = owtime.owct.OWCT.now()

# 反推owct时间
backstep_owct_time = owtime.owct.OWCT.from_datetime(datetime.datetime.now())

# 获取owtime时间
get_owtime_time = owtime.owtimes.OWTime.now()

# 反推owtime时间
backstep_owtime_time = owtime.owtimes.OWTime.from_datetime(datetime.datetime.now())

# 获取owcl时间
get_owcl_time = owtime.owcl.OWCL.now()

# 反推owcl时间
backstep_owcl_time = owtime.owcl.OWCL.from_datetime(datetime.datetime.now())
