# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:35:28 2018

@author: K-AI_LAB
"""

"""
Info
=====
This Code for running trained model by ANN_NACA4
"""

import time
# Time to import tensorflow is too slow. 
# To check that time, time library imported at the first line
time_start = time.time()
time_start_init = time.time() 

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
plt.close()
import tensorflow as tf

direct_code = os.path.dirname(os.path.realpath('__file__'))
direct_saved=os.path.join(direct_code,"saved")
sys.path.append(direct_code)

#import Training
import NACA4_Rinput as Rin
import NACA4_message as msg


# Create ANN Structure
#def loading(inputvalue):
class N4_FCNN_Load():
    def __init__(self,No_model):     
        self.No_model = No_model
        
        ## Parameters ##
        var, val = Rin.Rinput(os.path.join(direct_code,'Input'),'input.txt',2)
        self.L_rate = float(val[4])
        self.n_input = int(val[2])
        self.n_output = int(val[3])
        self.No_HL = int(val[0])
        self.No_Neuron = int(val[1])
        self.Active_function = val[5]
        self.dtype = val[6]
        
    def built_model(self):
        tf.reset_default_graph()
        ## Prepare Data ##
        # Divide Dataset as a Training Data (75%) and Test Data (25%)
        # random_stata : Fix the Divide rule 
        #       (None - Divide method is always change when we run the code)
        
        ## ANN Structure ##
        # Set the number of neuron of each layer
    
        # Define the number of each neuron
        i=1
        while i < self.No_HL + 1:
            globals()['n_hidden'+str(i)] = self.No_Neuron # nth hiddenlayer's number of neuron
            i += 1
    
        # Input and Output Layer
        if self.dtype == 'float32' or 'FP32':
            self.X = tf.placeholder(tf.float32, [None, self.n_input],name='x_input')
            self.Y = tf.placeholder(tf.float32, [None, self.n_output],name='y_input')
            
            # Initialize Weight
            # Initialize: Xavier Initializer        
            i=1
            while i < self.No_HL + 1:
                if i==1:
                    globals()['w'+str(i)] = tf.get_variable("Weight_"+str(i),shape=[self.n_input, globals()['n_hidden'+str(i)]],initializer=tf.contrib.layers.xavier_initializer())  # 1st hidden layer
                else:
                    globals()['w'+str(i)] = tf.get_variable("Weight_"+str(i),shape=[globals()['n_hidden'+str(i-1)], globals()['n_hidden'+str(i)]],initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
                i += 1
            
            # This is for a output layer
            globals()['wo'] = tf.get_variable("Weight_"+str(i),shape=[globals()['n_hidden'+str(i-1)], self.n_output],initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
    
            # Initialize Biasis
            # Initialize: Xavier Initializer
            i=1
            while i < self.No_HL + 1:
                if i==1:
                    globals()['b'+str(i)] = tf.get_variable("Bias_"+str(i),shape=[globals()['n_hidden'+str(i)]],initializer=tf.contrib.layers.xavier_initializer())  # 1st hidden layer
                else:
                    globals()['b'+str(i)] = tf.get_variable("Bias_"+str(i),shape=[ globals()['n_hidden'+str(i)]],initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
                i += 1
            
            # This is for a output layer
            globals()['bo'] = tf.get_variable("Bias_"+str(i),shape=[ self.n_output],initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
            
        elif self.dtype == 'float16' or 'FP16':
            self.X = tf.placeholder(tf.float16, [None, self.n_input],name='x_input')
            self.Y = tf.placeholder(tf.float16, [None, self.n_output],name='y_input')
            # Initialize: Xavier Initializer        
            i=1
            while i < self.No_HL + 1:
                if i==1:
                    globals()['w'+str(i)] = tf.get_variable("Weight_"+str(i),shape=[self.n_input, globals()['n_hidden'+str(i)]],dtype=tf.float16,initializer=tf.contrib.layers.xavier_initializer())  # 1st hidden layer
                else:
                    globals()['w'+str(i)] = tf.get_variable("Weight_"+str(i),shape=[globals()['n_hidden'+str(i-1)], globals()['n_hidden'+str(i)]],dtype=tf.float16,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
                i += 1
            
            # This is for a output layer
            globals()['wo'] = tf.get_variable("Weight_"+str(i),shape=[globals()['n_hidden'+str(i-1)], self.n_output],dtype=tf.float16,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
    
            # Initialize Biasis
            # Initialize: Xavier Initializer
            i=1
            while i < self.No_HL + 1:
                if i==1:
                    globals()['b'+str(i)] = tf.get_variable("Bias_"+str(i),shape=[globals()['n_hidden'+str(i)]],dtype=tf.float16,initializer=tf.contrib.layers.xavier_initializer())  # 1st hidden layer
                else:
                    globals()['b'+str(i)] = tf.get_variable("Bias_"+str(i),shape=[ globals()['n_hidden'+str(i)]],dtype=tf.float16,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
                i += 1
            
            # This is for a output layer
            globals()['bo'] = tf.get_variable("Bias_"+str(i),shape=[ self.n_output],dtype=tf.float16,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer        
            
            
        elif self.dtype == 'float64'  or 'FP64':
            self.X = tf.placeholder(tf.float64, [None, self.n_input],name='x_input')
            self.Y = tf.placeholder(tf.float64, [None, self.n_output],name='y_input')
            # Initialize: Xavier Initializer        
            i=1
            while i < self.No_HL + 1:
                if i==1:
                    globals()['w'+str(i)] = tf.get_variable("Weight_"+str(i),shape=[self.n_input, globals()['n_hidden'+str(i)]],dtype=tf.float64,initializer=tf.contrib.layers.xavier_initializer())  # 1st hidden layer
                else:
                    globals()['w'+str(i)] = tf.get_variable("Weight_"+str(i),shape=[globals()['n_hidden'+str(i-1)], globals()['n_hidden'+str(i)]],dtype=tf.float64,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
                i += 1
            
            # This is for a output layer
            globals()['wo'] = tf.get_variable("Weight_"+str(i),shape=[globals()['n_hidden'+str(i-1)], self.n_output],dtype=tf.float64,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
    
            # Initialize Biasis
            # Initialize: Xavier Initializer
            i=1
            while i < self.No_HL + 1:
                if i==1:
                    globals()['b'+str(i)] = tf.get_variable("Bias_"+str(i),shape=[globals()['n_hidden'+str(i)]],dtype=tf.float64,initializer=tf.contrib.layers.xavier_initializer())  # 1st hidden layer
                else:
                    globals()['b'+str(i)] = tf.get_variable("Bias_"+str(i),shape=[ globals()['n_hidden'+str(i)]],dtype=tf.float64,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer
                i += 1
            
            # This is for a output layer
            globals()['bo'] = tf.get_variable("Bias_"+str(i),shape=[ self.n_output],dtype=tf.float64,initializer=tf.contrib.layers.xavier_initializer())  # nth hidden layer        
            
        else:
            message = 'Check the Float_Precision in input.txt file'
            msg.debuginfo(message)
            
    def MP(self):
        
        i = 1
        message = str('Activation function: {}'.format(self.Active_function))
        msg.debuginfo(message)
        while i < self.No_HL + 1:
            if i == 1:
                vars()['HL'+str(i)] = tf.add(tf.matmul(self.X, globals()['w'+str(i)]),globals()['b'+str(i)])
                # Layer Normalization
                vars()['NL'+str(i)] = tf.contrib.layers.layer_norm(vars()['HL'+str(i)],center=True,scale=True)
                
                # Activation
                if self.Active_function == 'ReLU' or 'relu':
                    vars()['AL'+str(i)]=tf.nn.relu(vars()['NL'+str(i)])
                elif self.Active_function == 'ELU' or 'elu':
                    vars()['AL'+str(i)]=tf.nn.elu(vars()['NL'+str(i)])
                elif self.Active_function == 'Identiyu' or 'I':
                    vars()['AL'+str(i)]=vars()['NL'+str(i)]
                elif self.Active_function == 'Softplus' or 'softplus':
                    vars()['AL'+str(i)]=tf.nn.softplus(vars()['NL'+str(i)])
                    
                    
            elif i > 1:
                vars()['HL'+str(i)] = tf.add(tf.matmul(vars()['AL'+str(i-1)], globals()['w'+str(i)]),globals()['b'+str(i)])
                # Layer Normalization
                vars()['NL'+str(i)] = tf.contrib.layers.layer_norm(vars()['HL'+str(i)],center=True,scale=True)
                
                # Activation
                if self.Active_function == 'ReLU' or 'relu':
                    vars()['AL'+str(i)]=tf.nn.relu(vars()['NL'+str(i)])
                elif self.Active_function == 'ELU' or 'elu':
                    vars()['AL'+str(i)]=tf.nn.elu(vars()['NL'+str(i)])
                elif self.Active_function == 'Identiyu' or 'I':
                    vars()['AL'+str(i)]=vars()['NL'+str(i)]
                elif self.Active_function == 'Softplus' or 'softplus':
                    vars()['AL'+str(i)]=tf.nn.softplus(vars()['NL'+str(i)])
                    
            i += 1
        # Output layer
        
        if self.Active_function == 'ReLU' or 'relu':
            Out=tf.nn.relu(tf.add(tf.matmul(vars()['AL'+str(i-1)], globals()['wo']),globals()['bo']))
        elif self.Active_function == 'ELU' or 'elu':
            Out=tf.nn.elu(tf.add(tf.matmul(vars()['AL'+str(i-1)], globals()['wo']),globals()['bo']))
        elif self.Active_function == 'Identiyu' or 'I':
            Out=tf.add(tf.matmul(vars()['AL'+str(i-1)], globals()['wo']),globals()['bo'])
        elif self.Active_function == 'Softplus' or 'softplus':
            Out=tf.nn.softplus(tf.add(tf.matmul(vars()['AL'+str(i-1)], globals()['wo']),globals()['bo']))
        
        return Out


    def Normalize(self,data,scale):
        var, val = Rin.Rinput(direct_saved,'Normalization'+str(self.No_model)+'.txt',1)
        return_val = Rin.Conv_vals(var, val)
        data_avg = return_val[0]
        data_min = return_val[1]
        data_max = return_val[2]
        Ndata=data.copy()
        # Normalize Calculation
        #   Average :Zero
        #   Min, Max: - scale, scale
        i=0
        
        while i < np.shape(data)[0]:
            Ndata[i]=(data[i]-data_avg[i])/(data_max[i]-data_min[i])
            i += 1
        
        return scale*Ndata
#    
        
    def init_Run_ANN(self, x, Proc = 'GPU'):      
        
        if Proc == 'CPU':
            msg.debuginfo('CPU')
            with tf.device('/device:CPU:0'):
                self.built_model()
                self.logits = self.MP()
                saver = tf.train.Saver()
                Nx = np.expand_dims(self.Normalize(x,1),axis=0)
            self.sess = tf.Session(config = tf.ConfigProto(device_count={'CPU':1, 'GPU':0}, log_device_placement=True))
            saver.restore(self.sess,'./saved/model'+str(self.No_model))
            ## Active the code below, if you want to see the device log ##
#            options = tf.RunOptions(output_partition_graphs=True)
#            metadata = tf.RunMetadata()
#            y = self.sess.run(self.logits,feed_dict={self.X: Nx}, options=options, run_metadata=metadata)
#            msg.debuginfo(str(metadata.partition_graphs))
            ## If you don't want to see the log, activate below ##            
            y = self.sess.run(self.logits,feed_dict={self.X: Nx})
           
        elif Proc == 'GPU':
            with tf.device('/device:GPU:0'):
                self.built_model()
                self.logits = self.MP()
                saver = tf.train.Saver()
                Nx = np.expand_dims(self.Normalize(x,1),axis=0)
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.Session(config = tf.ConfigProto(log_device_placement=True))
            saver.restore(self.sess,'./saved/model'+str(self.No_model))
            ## Active the code below, if you want to see the device log ##
#            options = tf.RunOptions(output_partition_graphs=True)
#            metadata = tf.RunMetadata()
#            y = self.sess.run(self.logits,feed_dict={self.X: Nx}, options=options, run_metadata=metadata)
#            msg.debuginfo(str(metadata.partition_graphs))
            ## If you don't want to see the log, activate below ##
            y = self.sess.run(self.logits,feed_dict={self.X: Nx})
#            print(y)
#        print('init ANN')
        return y
    
    def Run_ANN(self, x):  
        ## If you want to check the time for prediction, Activate below 3 lines ##
#        time_start = time.time()              
        Nx = np.expand_dims(self.Normalize(x,1),axis=0)
        y = self.sess.run(self.logits,feed_dict={self.X: Nx})
#        time_predict = time.time() - time_start
#        print('Prediction time: {}'.format(time_predict))
        
        return y

if __name__ == "__main__":
    
    ANN = N4_FCNN_Load(20)

    time_start = time.time()
    x = np.array([0.24270,   0.10440,   0.00570,  -0.05200,  0.00220])
    y = ANN.init_Run_ANN(x,'GPU')
    
    time_predict = time.time() - time_start
    print(time_predict)
#    
#    time_start = time.time()
#    x = np.array([0.8025, 0.0044, 0.01402, -0.2529, 0.015])
#    y = ANN.init_Run_ANN(x,'GPU')
#    time_predict = time.time() - time_start
#    print(time_predict)
#    
#    time_start = time.time()
#    x = np.array([0.24270,   0.10440,   0.00570,  -0.05200,  0.00220])
#    y = ANN.Run_ANN(x)
#    time_predict = time.time() - time_start
#    print(time_predict)
#    def Run_ANN(self, x, Proc = 'CPU'):      
#        self.built_model()
#        logits = self.MP()
#        saver = tf.train.Saver()
#        Nx = np.expand_dims(self.Normalize(x,1),axis=0)
#        
#        if Proc == 'CPU':
#            config = tf.ConfigProto(device_count={'CPU' : 1, 'GPU' : 0}, allow_soft_placement=True,log_device_placement=True)
#            with tf.Session(config = config) as sess:
#                with tf.device('/CPU:0'):
#                    sess.run(tf.global_variables_initializer())
#                    saver.restore(sess,'./saved/model'+str(self.No_model))
#                    
#                    ## Active the code below, if you want to see the device log ##
##                    options = tf.RunOptions(output_partition_graphs=True)
##                    metadata = tf.RunMetadata()
##                    y = sess.run(logits,feed_dict={self.X: Nx}, options=options, run_metadata=metadata)
##                    msg.debuginfo(str(metadata.partition_graphs))
##           
#                    y = sess.run(logits,feed_dict={self.X: Nx})
#                    
#        elif Proc == 'GPU':
#            config = tf.ConfigProto(device_count={'CPU' : 1, 'GPU' : 1}, allow_soft_placement=True,log_device_placement=False)
#            config.gpu_options.allow_growth = True
#            
#            with tf.Session(config = config) as sess:
#                with tf.device('/GPU:0'):
#                    sess.run(tf.global_variables_initializer())
#                    saver.restore(sess,'./saved/model'+str(self.No_model))
#                    
#                    ## Active the code below, if you want to see the device log ##
##                    options = tf.RunOptions(output_partition_graphs=True)
##                    metadata = tf.RunMetadata()
##                    y = sess.run(logits,feed_dict={self.X: Nx}, options=options, run_metadata=metadata)
##                    msg.debuginfo(str(metadata.partition_graphs))
#                    
#                    y = sess.run(logits,feed_dict={self.X: Nx})
#           
#        return y
#
#if __name__=="__main__":
#    ANN = N4_FCNN_Load(20)
#    
#    time_import_tf = time.time() - time_start
#    
#    message = str("Import time: {:.4f} mili sec, {:.4f} sec".format(time_import_tf*1000, time_import_tf))
#    msg.debuginfo(message)
#    
#    time_start = time.time()
#    
#    
#    # Initial configuration
#    #x = np.array([0.7125,   0.01566,   0.01326,  -0.20265,   -0.006])
#    x = np.array([0.24270, 0.10440, 0.00570, -0.05200, 0.00220])
#    y = ANN.Run_ANN(x,'GPU')
#    
#    time_predict = time.time() - time_start
#    
#    message = str("DLED Prediction\n - Max. Camber: {:.4f}\n - Max. Loc. Camber: {:.4f}\n - Max. Thickness: {:.4f}\n".format(y[0,0],y[0,1],y[0,2]))
#    msg.debuginfo(message)
#    message = str("Design time: {:.4f} mili sec, {:.4f} sec".format(time_predict*1000, time_predict))
#    msg.debuginfo(message)
#    
#    time_start = time.time()
#    
#    Resultdirect = os.path.join(direct_code,"Result")
#    Config.NACA4(160,y[0,0],y[0,1],y[0,2],Resultdirect)
#    RunXfoil.runXFOIL_Restore()
#    Aero_predicted_config = CalAero.run_Restore()
#    Error_Aero = x-Aero_predicted_config
#    
#    time_Analysis = time.time() - time_start
#    time_processing = time.time() - time_start_init
#    
#    message = str("Re_Analysis time: {:.4f} mili sec, {:.4f} sec".format(time_Analysis*1000, time_Analysis))
#    msg.debuginfo(message)
#    message = str("Run time: {:.4f} mili sec, {:.4f} sec".format(time_processing*1000, time_processing))
#    msg.debuginfo(message)