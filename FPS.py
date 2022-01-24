import time
class FPS:
    def __init__(self) :

        self._tick2_frame=0
        self._tick2_fps=20000000 # real raw FPS
        self._tick2_t0=time.time()

    def fpsLimit(self,fps=60):
        global _tick2_frame,_tick2_fps,_tick2_t0
        n=self._tick2_fps/fps
        self._tick2_frame+=n
        while n>0: n-=1
        if time.time()-self._tick2_t0>1:
            _tick2_t0=time.time()
            _tick2_fps=self._tick2_frame
            _tick2_frame=0



