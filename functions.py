import ctypes 
import os
os.chdir("./")

def race_step(laps:int, prob:float, rate:float):
    
    """ Step for a race simulation
    """
    
    clibrary = ctypes.CDLL('F:/Python/proyectos/F1/functions.dll')
    box_probability = clibrary.box_probability
    box_probability.argtypes = [ctypes.c_double, ctypes.c_int, ctypes.c_double]
    box_probability.restype = ctypes.c_double
    
    prob = box_probability(prob, laps, rate)
    
    clibrary = ctypes.CDLL('F:/Python/proyectos/F1/functions.dll')
    box_eval = clibrary.box_eval
    box_eval.argtypes = [ctypes.c_double]
    box_eval.restype = ctypes.c_bool
    
    decision = box_eval(prob)
    
    if decision:
        prob = 1
        laps = 0
    
    laps += 1
    
    return prob, laps, decision
        
        
        
    
        


if __name__ == "__main__":
    None