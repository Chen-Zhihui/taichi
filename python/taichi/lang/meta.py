import taichi as ti

# A set of helper (meta)functions


@ti.kernel
def fill_tensor(tensor: ti.template(), val: ti.template()):
  for I in ti.grouped(tensor):
    tensor[I] = val


@ti.kernel
def tensor_to_ext_arr(tensor: ti.template(), arr: ti.ext_arr()):
  for I in ti.grouped(tensor):
    arr[I] = tensor[I]


@ti.kernel
def ext_arr_to_tensor(arr: ti.ext_arr(), tensor: ti.template()):
  for I in ti.grouped(tensor):
    tensor[I] = arr[I]
    
