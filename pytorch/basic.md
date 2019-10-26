
> ​	pytorch  is just a replacement for numpy to use the power of GPU , also a deep learning research platform that provide maximum flexible and speed .

## Tensor

Tensors are similar to numpy 's ndarrays ,tensors can also be used on a GPU to accelerate computing.

- Construct a randomly initalize matrix 

  - ```python
    x=torch.rand(6,3)
    y=torch.zeros(5,3,dtype=torch.long)
    z=torch.tensor([5.5,3])
    ```

    

- create a Tensor based on existing Tensor,this will reuse properties of the input tensor 

  - ```python 
    x=torch.ones(3,3,dtype=torch.float)
    y=torch.rand_like(x)
    ```

- Operations 

  - sum

  - slice

  - if you want to resize/reshape Tensor , you can use **torch .view **

  - if you want change tensor as python number you can use **.item**,but be careful  **only one tensor can be change into python number**

    ```python 
    x=torch.rand(1)
    x.item()
    ```

    

## Numpy bridge 

- coverting a torch tensor to a numpy array 

  - ```python
    a=torch.rand(5)
    b=a.numpy()
    ```

- converting numpy array to torch tensor 

  - ```python
    a=np.ones(5)
    b=torch.from_numpy(a)
    ```

    

# AUTOGRAD : AUTOMATIC DIFFERENTIATION

## preview

- if you set its attribute *.requires_grad* is *True* , it starts to track all operation  on it .you can use *backward()* and have all the gradients computed automatically .

- You can call *.detach()* to detach it from computation history , and to prevent future computation from being tracked , also you can wrap the code block in *with torch .no_grad()*

- tensor and function are interconnected  and build up an acyclic graph(非循环图)，that encodes a computation 

- if you want to compute the derivative ,you just call backward() if your tensor is a scalar ,however if you has more elements ,you have a lot to do.

  ```python
  x=torch.ones(2,2,requires_grad=True)
  y=x+2
  
  #do more operations on y
  z=y*3*3
  
  #Figure out the mean
  out=z.mean()
  
  #It is that z is just a scalar so we can use backward() to figure out derivative.
  out.backward()
  x.grad
  
  ======
  tensor([[2.2500, 2.2500],
          [2.2500, 2.2500]])
  ======
  ```
  