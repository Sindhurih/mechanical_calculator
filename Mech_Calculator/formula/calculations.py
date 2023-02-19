import math


def cal_cylinder_velocity(form):
    flow_rate = form.cleaned_data['flow_rate']
    area = form.cleaned_data['area']
    result = (flow_rate * 0.3208)/area
    r=round(result,5)
    return str(r) + ' ft/sec'


def cal_Cylinder_Volume_Capacity(form):
    area = form.cleaned_data['area']
    stroke = form.cleaned_data['stroke']
    result = (area*stroke)/231
    r = round(result,5)
    return str(r) + ' Gallons of fluid'

def cal_Cylinder_flow_rate(form):
    velocity = form.cleaned_data['velocity']
    area = form.cleaned_data['area']
    result = velocity*area*3.117
    r = round(result, 5)
    return str(r) + ' GPM'

def cal_Cylinder_fluid_motor_torque(form):
    pressure = form.cleaned_data['pressure']
    displacement = form.cleaned_data['displacement']
    result = (pressure*displacement)/6.2831853
    r=round(result,5)
    return str(r)+' lbs'

def cal_Cylinder_fluid_motor_speed(form):
    flow_rate = form.cleaned_data['flow_rate']
    displacement = form.cleaned_data['displacement']
    result = (flow_rate*231)/displacement
    r=round(result,5)
    return str(r)+ ' RPM'


def cal_fluid_motor_power(form):
    torque = form.cleaned_data['torque']
    RPM = form.cleaned_data['RPM']
    result = (torque*RPM)/63025
    r = round (result, 5)
    return str(r) +' hp'

def cal_Bearing_length(form):
    load = form.cleaned_data['load']
    pressure = form.cleaned_data['pressure']
    diameter = form.cleaned_data['diameter']
    result = load/(pressure*diameter)
    r = round (result, 5)
    return str(r) +' in'

def cal_Bearing_heat_generation(form):
    load = form.cleaned_data ['load']
    diameter = form.cleaned_data ['diameter']
    RPM = form.cleaned_data ['RPM']
    friction=form.cleaned_data['friction']
    result=(friction*load*diameter*RPM)/50
    r = round (result, 5)
    return str(r) + ' BTU/h'

def cal_Bearing_wall_area(form):
    factor=form.cleaned_data['factor']
    length=form.cleaned_data['length']
    diameter = form.cleaned_data ['diameter']
    result=(factor*length*diameter)/144
    r = round (result, 5)
    return str(r) +' in^2'

def cal_Bearing_life_in_revolution(form):
    dynamic_capacity=form.cleaned_data['dynamic_capacity']
    radial_load=form.cleaned_data['radial_load']
    result=(dynamic_capacity/radial_load)**(10/3)
    r = round (result, 5)
    return str(r) + ' rev'

def cal_Bearing_heat_dissipation(form):
    Wall_area=form.cleaned_data['Wall_area']
    bearing_temperature=form.cleaned_data['bearing_temperature']
    outside_temperature=form.cleaned_data['outside_temperature']
    result=(Wall_area*2.2)*(bearing_temperature-outside_temperature)
    r = round (result, 5)
    return str(r) + ' BTU'

def cal_Bearing_Fluid_Motor_Power(form):
    torque=form.cleaned_data['torque']
    rpm=form.cleaned_data['rpm']
    result=(torque*rpm)/63025
    r = round (result, 5)
    return str(r) + ' hp'


def cal_Fluid_Pressure(form):
    force=form.cleaned_data['force']
    area=form.cleaned_data['area']
    result = force/area
    r = round (result, 5)
    return str(r) + ' psi'

def cal_Fluid_power(form):
    pressure=form.cleaned_data['pressure']
    flow=form.cleaned_data['flow']
    result=(pressure*flow)/1714
    r = round (result, 5)
    return str(r) + ' hp'

def cal_Compressibility_of_a_fluid(form):
    bulk_modulus=form.cleaned_data['bulk_modulus']
    result=1/bulk_modulus
    r = round (result, 5)
    return str(r) + ''

def cal_Specific_gravity_of_fluid(form):
    weight=form.cleaned_data['weight']
    result=weight/62.4283
    r = round (result, 5)
    return str(r) + ''


def cal_Hydraulic_Horsepower(form):
    pressure = form.cleaned_data ['pressure']
    oil_flow = form.cleaned_data ['oil_flow']
    result=(pressure*oil_flow)/1714
    r = round (result, 5)
    return str(r) + ' hp'

def cal_Heat_Equivalent_of_fluid_power(form):
    pressure = form.cleaned_data ['pressure']
    oil_flow = form.cleaned_data ['oil_flow']
    result=(pressure*oil_flow*1.5)
    r = round (result, 5)
    return str(r) +' BTU/hr'

def cal_Storage_capacity_of_cylindrical_tank(form):
    length = form.cleaned_data ['length']
    diameter = form.cleaned_data ['diameter']
    result=3.142*diameter*length
    r = round (result, 5)
    return str(r)+ ' in^3'

def cal_First_law_of_thermodynamics(form):
    u=form.cleaned_data['u']
    w=form.cleaned_data['w']
    result=u+w
    r = round (result, 5)
    return str(r) + ' J'

def cal_Adiabatic_process(form):
    n=form.cleaned_data['n']
    Ti=form.cleaned_data['Ti']
    Tf=form.cleaned_data['Tf']
    Y=form.cleaned_data['Y']
    result=(n*8.3*(Ti-Tf))/Y-1
    r = round (result, 5)
    return str(r) + ' J'

def cal_Isobaric_process(form):
    P=form.cleaned_data['P']
    V=form.cleaned_data['V']
    result=(P*V)
    r = round (result, 5)
    return str(r) +' J'

def cal_Second_law_of_Thermodynamics(form):
    dQ=form.cleaned_data['dQ']
    T=form.cleaned_data['T']
    result=dQ/T
    r = round (result, 5)
    return str(r) +' J/K'

def cal_V_Belt_Calculator(form):
    r1=form.cleaned_data['r1']
    r2=form.cleaned_data['r2']
    d=form.cleaned_data['d']
    result=3.142*(r1+r2)+2*3+(r1-r2)/d
    r = round (result, 5)
    return str(r) + ' ft/sec'

def cal_Storage_Capacity_Of_Rectangular_Tank(form):
    l=form.cleaned_data['l']
    w=form.cleaned_data['w']
    h=form.cleaned_data['h']
    result=(l*w*h)/231
    r = round (result, 5)
    return str(r) +' liters'

def cal_Pipe_friction_loss(form):
    f=form.cleaned_data['f']
    L=form.cleaned_data['L']
    D=form.cleaned_data['D']
    V=form.cleaned_data['V']
    g=form.cleaned_data['g']
    result=(f*(L/D)*(pow(V,2))/2*g)
    r = round (result, 5)
    return str(r) + ' m'

def push_and_pull_calc(form):
    bore = form.cleaned_data['bore']
    p = form.cleaned_data['pressure']
    d = form.cleaned_data['diameter']
    push_r = (p*3.1415*bore*bore)/4
    pull_r = (p*3.1415*(bore*bore - d*d))/4
    data = {'push_r': push_r, 'pull_r': pull_r}
    print(data)
    return data

def cal_pipe_enlargement(form):
    t=form.cleaned_data['t']
    B=form.cleaned_data['B']
    if t > 45:
        K = pow((1 - B ^ 2), 2)
    else:
        K = 2.6 * math.sin(t / 2) * pow((1 - B ^ 2), 2)
    return K

