import exifread
import datetime
# 使用 exifread 获取图片的元数据
img_exif = exifread.process_file(open('111.png', 'rb'),details=False, strict=True)

# 能够读取到属性

# 纬度数
latitude_gps = img_exif['GPS GPSLatitude']

# N,S 南北纬方向
latitude_direction = img_exif['GPS GPSLatitudeRef']

# 经度数
longitude_gps = img_exif['GPS GPSLongitude']

# E,W 东西经方向
longitude_direction = img_exif['GPS GPSLongitudeRef']

# 拍摄时间
take_time = img_exif['EXIF DateTimeOriginal']

def judge_time_met(take_time):
    """
    判断拍摄时间是否是在今天
    :param take_time:
    :return:
    """
    # 拍摄时间
    format_time = str(take_time).split(" ")[0].replace(":", "-")

    # 当天日期
    today = str(datetime.date.today())

    if format_time == today:
        print('拍摄于今天')
    else:
        print('很遗憾的通知你，你的女朋友在撒谎！！！')

judge_time_met(take_time)

