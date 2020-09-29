import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt



def Variable1(vX):
    return vX

def Variable2(vY):
    return vY

def Variable3(x,y):
    M=5.97e24
    r=((x**2)+((y)**2))*np.sqrt((x**2)+((y)**2))
    return ((-1)*sc.G*M*x)/(r)

def Variable4(x,y):
    M=5.97e24
    r=((x**2)+((y)**2))*np.sqrt((x**2)+((y)**2))
    return ((-1)*sc.G*M*y)/(r)

def RK4():
    
    M=5.97e24
    x=[0]
    y=[Initial_Radius+ 6.371E6]
    vX=[Initial_Velocity]
    vY=[0]
    t=[0]
    i=0
    KE=[(0.5)*(vX[i]**2+vY[i]**2)]
    PE=[((-sc.G*M)/(np.sqrt(x[i]**2+y[i]**2)))]
    E=[(KE[i]+PE[i])]
    
    while t[i]<=Tf:
        
        k1x=Variable1(vX[i])
        k1y=Variable2(vY[i])
        k1vX=Variable3(x[i],y[i])
        k1vY=Variable4(x[i],y[i])
    
        k2x=Variable1(vX[i]+((h/2)*k1vX))
        k2y=Variable2(vY[i]+((h/2)*k1vY))
        k2vX=Variable3(x[i]+(h/2)*k1x, y[i]+(h/2)*k1y)
        k2vY=Variable4(x[i]+(h/2)*k1x, y[i]+(h/2)*k1y)
    
        k3x=Variable1(vX[i]+((h/2)*k2vX))
        k3y=Variable2(vY[i]+((h/2)*k2vY))
        k3vX=Variable3(x[i]+(h/2)*k2x,y[i]+(h/2)*k2y)
        k3vY=Variable4(x[i]+(h/2)*k2x,y[i]+(h/2)*k2y)
    
        k4x=Variable1(vX[i]+h*k3vX)
        k4y=Variable2(vY[i]+h*k3vY)
        k4vX=Variable3(x[i]+h*k3x,y[i]+h*k3y)
        k4vY=Variable4(x[i]+h*k3x,y[i]+h*k3y)
    
       
        x.append(x[i]+((h/6)*((k1x)+(2*k2x)+(2*k3x)+(k4x))))
        y.append(y[i]+((h/6)*((k1y)+(2*k2y)+(2*k3y)+(k4y))))
        vX.append(vX[i]+((h/6)*((k1vX)+(2*k2vX)+(2*k3vX)+(k4vX))))
        vY.append(vY[i]+((h/6)*((k1vY)+(2*k2vY)+(2*k3vY)+(k4vY))))
        KE.append((1/2)*(vX[i]**2+vY[i]**2))
        PE.append((-sc.G*M)/(np.sqrt(x[i]**2+y[i]**2)))
        E.append(KE[i]+PE[i])
        t.append(t[i]+h)
        
        if abs(np.sqrt(x[i]**2+y[i]**2))<=6.38e6:
            print("The projectile has crashed on Earth!!! :0")
            break
        
        i+=1
        
    return x,y,vX,vY,KE,PE,E,t


def Variable3_Moon(x,y):
    
    d=3.84e8
    M=5.97e24
    M_Moon=7.35e22
    r=((x**2)+((y)**2))*np.sqrt((x**2)+((y)**2))
    r_Moon=(((x-d)**2)+((y)**2))*np.sqrt(((x-d)**2)+((y)**2))
    return ((-1)*sc.G*M*x)/(r)-(sc.G*M_Moon*(x-d))/(r_Moon)

def Variable4_Moon(x,y):
    
    d=3.84e8
    M=5.97e24
    M_Moon=7.35e22
    r=((x**2)+((y)**2))*np.sqrt((x**2)+((y)**2))
    r_Moon=(((x-d)**2)+((y)**2))*np.sqrt(((x-d)**2)+((y)**2))
    return ((-1)*sc.G*M*y)/(r)-(sc.G*M_Moon*(y))/(r_Moon)

def RK4_Moon():
    
    M=5.97e24
    d=3.84e8
    x=[-(Initial_Radius+6.38e6)]
    y=[0]
    vX=[0]
    vY=[Initial_Velocity]
    t=[0]
    i=0
    KE=[(0.5)*(vX[i]**2+vY[i]**2)]
    PE=[((-sc.G*M)/(np.sqrt(x[i]**2+y[i]**2)))+((-sc.G*M)/(np.sqrt((x[i]-d)**2+y[i]**2)))]
    E=[(KE[i]+PE[i])]
    
    while t[i]<=Tf:
        
        k1x=Variable1(vX[i])
        k1y=Variable2(vY[i])
        k1vX=Variable3_Moon(x[i],y[i])
        k1vY=Variable4_Moon(x[i],y[i])
    
        k2x=Variable1(vX[i]+((h/2)*k1vX))
        k2y=Variable2(vY[i]+((h/2)*k1vY))
        k2vX=Variable3_Moon(x[i]+(h/2)*k1x, y[i]+(h/2)*k1y)
        k2vY=Variable4_Moon(x[i]+(h/2)*k1x, y[i]+(h/2)*k1y)
    
        k3x=Variable1(vX[i]+((h/2)*k2vX))
        k3y=Variable2(vY[i]+((h/2)*k2vY))
        k3vX=Variable3_Moon(x[i]+(h/2)*k2x,y[i]+(h/2)*k2y)
        k3vY=Variable4_Moon(x[i]+(h/2)*k2x,y[i]+(h/2)*k2y)
    
        k4x=Variable1(vX[i]+h*k3vX)
        k4y=Variable2(vY[i]+h*k3vY)
        k4vX=Variable3_Moon(x[i]+h*k3x,y[i]+h*k3y)
        k4vY=Variable4_Moon(x[i]+h*k3x,y[i]+h*k3y)
    
       
        x.append(x[i]+((h/6)*((k1x)+(2*k2x)+(2*k3x)+(k4x))))
        y.append(y[i]+((h/6)*((k1y)+(2*k2y)+(2*k3y)+(k4y))))
        vX.append(vX[i]+((h/6)*((k1vX)+(2*k2vX)+(2*k3vX)+(k4vX))))
        vY.append(vY[i]+((h/6)*((k1vY)+(2*k2vY)+(2*k3vY)+(k4vY))))
        KE.append((1/2)*(vX[i]**2+vY[i]**2))
        PE.append((-sc.G*M)/(np.sqrt(x[i]**2+y[i]**2)))
        E.append(KE[i]+PE[i])
        t.append(t[i]+h)
        
        if abs(np.sqrt(x[i]**2+y[i]**2))<=6.38e6:
            print("The projectile has crashed on Earth!!! :0")
            break
        if abs(y[i])<=1.7371e6 and x[i]>=(d-1.7371e6) and x[i]<=(d+1.7371e6):
            print("The projectile has crashed on the Moon!!! :/")
            break
        
        i+=1
        
    return x,y,vX,vY,KE,PE,E,t

MyInput=input("Enter a choice between 'a', 'b' or 'q' to quit: ")
print("You have enter : ",MyInput)
if MyInput=="a":
    
    Input_h=input("Enter a value for the time step of the calculations in seconds: ")
    h=float(Input_h)
    Input_Initial_Radius=input("Enter a value for the initial radius of the orbit: ")
    Initial_Radius=float(Input_Initial_Radius)
    Input_Initial_Velocity=input("Enter a value for the initial velocity of the projectile: ")
    Initial_Velocity=float(Input_Initial_Velocity)
    Input_Tf=input("Enter a time duration for the observation: ")
    Tf=int(Input_Tf)
    
    x,y,vX,vY,KE,PE,E,t=RK4()
    
    plt.plot(x,y)
    plt.xlabel("x (Horizontal) / m")
    plt.ylabel("y (Vertical) / m")
    Sketch_Earth=plt.Circle((0,0), radius=6.38e6)
    plt.gca().add_patch(Sketch_Earth)
    plt.axis("scaled")
    plt.show()

    plt.plot(t,KE,label="Kinetic Energy")
    plt.plot(t,PE,label="Potential Energy")
    plt.plot(t,E,label="Total Energy")
    plt.legend()
    plt.xlabel("Time / s")
    plt.ylabel("Relative Energy / J/kg")
    plt.show()


if MyInput=="b":
    
    Input_h=input("Enter a value for the time step of the calculations in seconds: ")
    h=float(Input_h)
    Initial_Radius=7000000
    Input_Initial_Velocity=input("Enter a value for the initial velocity of the projectile: ")
    Initial_Velocity=float(Input_Initial_Velocity)
    Input_Tf=input("Enter a time duration for the observation: ")
    Tf=int(Input_Tf)
    
    x,y,vX,vY,KE,PE,E,t=RK4_Moon()
    
    plt.plot(x,y)
    plt.xlabel("x (Horizontal) / m")
    plt.ylabel("y (Vertical) / m")
    Earth_Sketch=plt.Circle((0,0),radius=6.38e6)
    Moon_Sketch=plt.Circle((3.84e8,0),radius=1.7371e6)
    plt.gca().add_patch(Earth_Sketch)
    plt.gca().add_patch(Moon_Sketch)
    plt.axis("scaled")
    plt.show()
    
    plt.plot(t,KE,label="Kinetic Energy")
    plt.plot(t,PE,label="Potential Energy")
    plt.plot(t,E,label="Total Energy")
    plt.legend()
    plt.xlabel("Time / s")
    plt.ylabel("Relative Energy / J/kg")
    plt.show()   
    
    
if MyInput=="q":
    
    print("Goodbye!")