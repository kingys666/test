import os,time,sys
import win32com.client
def getPpt():
     files = os.listdir("./")
     return files
def init_powerpoint():
    powerpoint = win32com.client.Dispatch('PowerPoint.Application') #comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint
def ppt2mp4(ppt_path,powerpoint,fileName):
    try:
        ppt = powerpoint.Presentations.Open(ppt_path)
        quality = 60
        # resolution:The resolution of the slide. 480,720,1080...
        resolution = 1080
        # frames: The number of frames per second.
        frames = 24
        mp4_target = os.path.abspath('./'+fileName+'.mp4')
        print(mp4_target)
        print(fileName,"----正在转成视频")
        ppt.CreateVideo(mp4_target,-1,1,resolution,frames,quality)
        while True:
            try:
                time.sleep(0.1)
                if os.path.exists(mp4_target) and os.path.getsize(mp4_target) == 0:
                    # The filesize is 0 bytes when convert do
                    # not complete.
                    continue
                break
            except Exception as e:
                print (e)
                break
        ppt.Close()
    except IOError:
        print('PPT转png失败',ppt_path)
    else:
        print('\n')
        print('\n')
        print("PPT转mp4成功",ppt_path)

if __name__=='__main__':
    powerpoint = init_powerpoint()
    pptArr = getPpt()
    print('---pptArr--',pptArr)
    for index,value in enumerate(pptArr):
        if(('.ppt' in value) ==True):
            _path = os.path.abspath('./'+value)
            fileName = os.path.basename(_path).split('.')[0]
            ppt2mp4(_path, powerpoint, fileName)
        time.sleep(2)
    powerpoint.Quit()
    input("输入任意键结束")

