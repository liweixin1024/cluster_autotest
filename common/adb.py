import os
import subprocess
from datetime import datetime

class adb():
    """
    adb相关命令操作
    """
    @staticmethod
    def adb_pull(devices:str,source:str,dest:str):
        """
        导出安卓文件
        parame: devices: 设备地址通过adb devices获得
        parame: source: 安卓路径
        parame: dest: 本地路径
        """
        command = "adb -s {} pull {} {}".format(devices,source,dest)
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.stdin.close()
        process.wait()

    @staticmethod
    def adb_pull_image(devices:str,source:str,dest:str):
        """
        导出安卓下图片,主要用于导出仪表截图,并返回截图路径
        parame: devices: 设备地址通过adb devices获得
        parame: source: 安卓路径
        parame: dest: 本地路径
        """
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y%m%d-%H%M%S")
        command = "adb -s {} pull {} {}-{}".format(devices,source,dest,formatted_time)
        #process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        #process.stdin.close()
        #process.wait()
        

test = adb.adb_pull_image("test","test","test",)