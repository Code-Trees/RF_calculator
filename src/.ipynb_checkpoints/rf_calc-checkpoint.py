import pandas as pd
import tabulate

#OutPut Image shape calculator

def ch_out(ch_in,pad,kern,strid):
    CH_out =((ch_in+2*pad - kern)/strid)+1
    return int(CH_out)

#Jump calculator
def jp_out(jp_in,strid):
    JP_out = jp_in*strid
    return int(JP_out)

#Receptive field out calculator
def Rf_out(rf_in,kern,jump_in):
    RF_out = rf_in+(kern-1)*jump_in
    return int(RF_out)


# Returns the Kernel Size,Stride Size, Padding Size 
def get_values(lar):
    st=[]
    pd = []
    lar = str(lar)
    for part in lar.split(' '):
        
        if "kernel_size" in part[0:12]:
            ker= part[-2]
        if "MaxPool2d" in part:
            ker = part[-2]
            
        if 'AdaptiveAvgPool2d' in part:
            ker = [i[-2] for i in part.split(' ') if 'output_size' in i][0]
            s = 1
            
        if 'stride' in part[0:7]:
            s = part[-2]

        if 'padding' in part:
            pd.append(int(part[-2]))
        else:
            pd.append(0)

    p = max(pd)
    return int(ker),int(s),int(p)

def model_df(model_object):
#     xml = dict2xml(model_object._dir_)
    model_layers = str(model_object.__dir__)
    search_keywords = {' MaxPoo',' Conv2d'}
    model_layers = str(model_object)
    req_layers = []
    for part in model_layers.split(':'):
        if part[0:7] in search_keywords:
            req_layers.append(str(part))
        if part[0:18] == ' AdaptiveAvgPool2d':
            req_layers.append(str(part))
            
    df = pd.DataFrame(req_layers,columns = ['layers'])
    return df



def receptive_field(model_obj,input_image,jump_in = 1,rf_in =1 ,):
    
    channel_in = input_image
    c = channel_in
    r = 1
    j = 1

    L = []
    K= []
    P = []
    S = []
    c_in = []
    C_out = []
    R_out = []
    
    model_data = model_df(model_obj)
    
    for i in model_data.layers:
        kernel,stride,padding = get_values(i)
#         print (kernel,padding,stride)
        
        channel_out  = ch_out(channel_in,padding,kernel,stride)    
        jump_out  =jp_out(jump_in,stride)   
        rf_out= Rf_out(rf_in,kernel,jump_in)

#         L.append('Layer_'+str(i))
#         L.append(name)
        K.append(str(kernel)+'*'+str(kernel))
        P.append(['NO' if padding == 0 else padding][0])
        S.append(stride)
        c_in.append(str(c)+ '*' + str(c))
        C_out.append(str(abs(channel_out))+ '*'+ str(abs(channel_out)))
        R_out.append(str(rf_out)+ '*'+ str(rf_out))


        rf_in =r = rf_out
        jump_in=j = jump_out
        channel_in=c = channel_out

    RF_graph = {'Kernel_size':K,'Padding':P,'Stride':S,'Input_Img_size':c_in,'Output_Img_size':C_out,'Receptive_field':R_out}
    RF = pd.DataFrame(RF_graph)
    
    print ("=======================================Reciptive Field Calculator========================================")
    print(RF.to_markdown())
    print ("=========================================================================================================")
    return RF

# error = receptive_field(model,input_image = 28)

# print (['No Error' if error == 0 else 'Somethign went wrong'][0])