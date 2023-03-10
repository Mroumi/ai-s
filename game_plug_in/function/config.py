"""
 游戏里实时修改 mouse_offset_ratio 的功能被我屏蔽了，因为有的小伙伴的按键设置和这个有冲突。
    需要相关功能的自行修改代码....  在function文件夹下的 mouse_controller.py 里，我有备注

"""
import os

root_dir_name = 'game_plug_in'
root_path = os.getcwd().split(root_dir_name)[0]  # game_plug_in 文件夹，不要随便改名字...

weights = f'{root_path}{root_dir_name}\model\PUBG.pt'  # 权重文件路径  看不懂的话只改 最后一个\后面的 文件名

grab_window_title = 'PUBG：绝地求生 '  # 这个地方写 游戏窗口的名字
screen_width, screen_height = 1920, 1080  # 屏幕分辨率
grab_width, grab_height = 640, 640  # 截图大小

top_window_width = 300  # 置顶 窗口大小
is_show_top_window = True  # 是否显示置顶窗口

mouse_offset_ratio = 0.5  # 鼠标偏移系数  取值0.2-1  数值越大，鼠标追人的速度越快

conf_thres = 0.5  # 置信度  检测到一个东西，这个东西可能是人的概率是多少。 比方程序说这个东西概率是0.28，你设置的这个值是0.25，那就会在结果框里显示这是个人。如果你设置的值大于0.28，结果框就忽略这个东西

show_list = ['person', 'body', 'head']  # 锁定对象的列表

# --- --- --- --- --- --- --- 分割线 --- --- --- 下面的参数应该不要改 --- --- --- --- --- --- #
# --- --- --- --- --- --- --- 分割线 --- --- --- 下面的参数应该不要改 --- --- --- --- --- --- #
# --- --- --- --- --- --- --- 分割线 --- --- --- 下面的参数应该不要改 --- --- --- --- --- --- #

cv2_wait_ms = 1  # 每次检测之后程序睡眠的时间   这个数字有点玄学，想不通。有人的改成20左右就能锁到人。
top_window_name = 'top_window'  # 置顶窗口的名字  不能是中文
shot_interval_time = 0.1  # 开枪时间间隔
data = f'{root_path}data\coco128.yaml'
imgsz = [640, 640]
iou_thres = 0.45  # 交并集
grab_rectangle = (int(screen_width / 2 - grab_width / 2), int(screen_height / 2 - grab_height / 2), grab_width, grab_height)
