import os
import torch
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


sources = ['src/reorg_cpu.c']
headers = ['src/reorg_cpu.h']
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/reorg_cuda.c']
    headers += ['src/reorg_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
# print(this_file)
extra_objects = ['src/reorg_cuda_kernel.cu.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

setup(
    name='reorg_layer',
    ext_modules=[
        CUDAExtension(
            '_ext.reorg_layer',
            headers=['header1.h', 'header2.h'],
            sources=['source1.cpp', 'source2.cu'],
            define_macros=[('WITH_CUDA', None)],
            extra_objects=[]  # 추가 오브젝트가 필요한 경우 여기에 추가
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)

if __name__ == "__main__":
    setup.py build
