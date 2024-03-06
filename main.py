import os
from multiprocessing import Process

def runrunaudio_script():
    os.system("python runmain.py")

# def runrunmovie_script():
#     os.system("python runmovie.py")

# def name_script():
#     os.system("python name.py")    

def delete_script():
    os.system("python delete.py")

if __name__ == "__main__":
    # name_process =  Process(target=name_script)
    # runrunmovie_process =  Process(target=runrunmovie_script)
    runrunaudio_process = Process(target=runrunaudio_script)
    delete_process = Process(target=delete_script)

    # name_process.start()
    # runrunmovie_process.start()
    runrunaudio_process.start()
    delete_process.start()

    try:
        # name_process.join()
        # runrunmovie_process.join()
        runrunaudio_process.join()
        delete_process.join()
    except KeyboardInterrupt:
        # name_process.terminate()
        # runrunmovie_process.terminate()
        runrunaudio_process.terminate()
        delete_process.terminate()
