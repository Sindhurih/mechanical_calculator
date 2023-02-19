from django.shortcuts import render, reverse

from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from formula import forms
from formula.calculations import *
# Create your views here.

CARD_TO_FORMULA = {
    'Actuator': {
        'cylinder_velocity': {
            'id': 1,
            'form': forms.CylinderVelocityForm,
            'name': 'Cylinder Velocity',
            'result': cal_cylinder_velocity,
            'output': 'Cylinder velocity',
            'formula': 'v = fr*0.3208/A',

        },
        'Cylinder_Volume_Capacity': {
            'id':2,
            'form': forms.CylinderVolumeCapacityForm,
            'name': 'Cylinder Volume Capacity',
            'result': cal_Cylinder_Volume_Capacity,
            'output': 'Cylinder Volume Capacity  (vc)',
            'formula': 'vc = A*Sr/231',
        },
        'Cylinder_flow_rate': {
            'id': 3,
            'form': forms.CylinderFlowRateForm,
            'name': 'Cylinder Flow Rate',
            'result': cal_Cylinder_flow_rate,
            'output': 'Cylinder Flow Rate (fr)',
            'formula': 'fr = v*A*3.117'
        },
        'Cylinder_fluid_motor_torque': {
            'id': 4,
            'form': forms.CylinderFluidMotorTorqueForm,
            'name': 'Cylinder Fluid Motor Torque',
            'result': cal_Cylinder_fluid_motor_torque,
            'output': 'Cylinder Fluid Motor Torque (t)',
            'formula': 't=(p*d)/6.2831853'
        },
        'Cylinder_fluid_motor_speed': {
            'id': 5,
            'form': forms.CylinderFluidMotorSpeedForm,
            'name': 'Cylinder Fluid Motor Speed',
            'result': cal_Cylinder_fluid_motor_speed,
            'output': 'Cylinder Fluid Motor Speed (s)',
            'formula': 's=(fr*231)/d'
        },
        'fluid_motor_power': {
            'id': 6,
            'form': forms.FluidMotorPowerForm,
            'name': 'Fluid Motor Power',
            'result': cal_fluid_motor_power,
            'output': 'Fluid Motor Power (fp)',
            'formula': 'fp = t*RPM/63025'

        },

    },

    'Bearing': {
        'Bearing_Length': {
            'id': 1,
            'form': forms.BearingLengthForm,
            'name': 'Bearing Length',
            'result': cal_Bearing_length,
            'output': 'Bearing length (l)',
            'formula': 'l=lo/(p*d)'
        },
        'Bearing_heat_generation': {
            'id': 2,
            'form': forms.BearingHeatGenerationForm,
            'name': 'Bearing Heat Generation',
            'result': cal_Bearing_heat_generation,
            'output': 'Bearing Heat Genearation (hg)',
            'formula': 'hg=(f*lo*d*RPM)/50'
        },
        'Bearing_wall_area': {
            'id': 3,
            'form': forms.BearingWallAreaForm,
            'name': 'Bearing Wall Area',
            'result': cal_Bearing_wall_area,
            'output': 'Bearing Wall Area (wa)',
            'formula': 'wa=(fc*l*d)/144'

        },
        'Bearing_life_in_revolution': {
            'id': 4,
            'form': forms.BearingLifeInRevolutionForm,
            'name':'Bearing Life in Revolution',
            'result':cal_Bearing_life_in_revolution,
            'output':'Bearing Life in Revolution (lr)',
            'formula':'lr=(dc/rl)pow(10/3)'
        },
        'Bearing heat dissipation': {
             'id': 5,
            'form': forms.BearingHeatDissipationForm,
            'name':'Bearing Heat Dissipation',
            'result': cal_Bearing_heat_dissipation,
            'output':'Bearing Heat Dissipation (hd)',
            'formula':'hd=(wa*2.2)*(t-ot)'

        },
        'Bearing Fluid Motor Power':{
            'id':6,
            'form':forms.BearingFluidMotorPowerForm,
            'name':'Bearing Fluid Motor Power',
            'result':cal_Bearing_Fluid_Motor_Power,
            'output':'Bearing Fluid Motor Power (fp)',
            'formula':'fp=Torque*RPM/63025'
        },
    },
    'Fluid Power': {
        'Fluid_Pressure': {
            'id': 1,
            'form': forms.FluidPressureForm,
            'name':'Fluid Pressure',
            'result':cal_Fluid_Pressure,
            'output':'Fluid Pressure (p)',
            'formula':'p=f/A'
        },
        'Fluid Power':{
            'id':2,
            'form':forms.FluidPowerForm,
            'name':'Fluid Power',
            'result':cal_Fluid_power,
            'output':'Fluid Power (fp)',
            'formula':'fp=(p*f)/1714'
        },
        'Compressibility of a fluid':{
            'id':3,
            'form':forms.CompressibilityOfaFluidForm,
            'name':'Compressibility of a Fluid',
            'result':cal_Compressibility_of_a_fluid,
            'output':'Compressibility of a fluid (cf)',
            'formula':'cf=1/(bm)'
        },
        'Specific Gravity of Fluid': {
            'id':4,
            'form':forms.SpecificGravityofFluidForm,
            'name':'Specific Gravity of Fluid',
            'result':cal_Specific_gravity_of_fluid,
            'output':'Specific Gravity of Fluid (sg)',
            'formula':'sg=w/62.4283'
        },
        'Hydraulic Horsepower':{
            'id':5,
            'form':forms.HydraulicHorsepowerForm,
            'name':'Hydraulic Horsepower',
            'result':cal_Hydraulic_Horsepower,
            'output':'Hydraulic Horsepower',
            'formula':'hp=(p*f)/1714'
        },
        'Heat Equivalent Of Fluid Power':{
            'id':6,
            'form':forms.HeatEquivalentOfFluidpowerForm,
            'name':'Heat Equivalent Of Fluid Power',
            'result':cal_Heat_Equivalent_of_fluid_power,
            'output':'Heat Equivalent Of Fluid Power (fp)',
            'formula':'fp=(f*p*1.5)'
        },
    },
    'Storage Capacity Of Cylindrical Tank':{
        'Storage Capacity Of Cylindrical Tank':{
        'id':1,
        'form':forms.StorageCapacityOfCylindricalTankForm,
        'name':'Storage Capacity Of Cylindrical Tank',
        'result':cal_Storage_capacity_of_cylindrical_tank,
        'output':'Storage Capacity Of Cylindrical Tank (sc)',
        'formula':'sc=3.142*d*l'
    },
},
    'Thermodynamics':{
        'First law of Thermodynamics': {
            'id':1,
            'form':forms.FirstLawOfThermodynamicsForm,
            'name':'First law of Thermodynamics',
            'result':cal_First_law_of_thermodynamics,
            'output':'First law of Thermodynamics (q)',
            'formula':'q=⍙U+W'
        },
        'Adiabatic Process': {
            'id':2,
            'form':forms.AdiabaticProcessForm,
            'name':'Adiabatic Process',
            'result':cal_Adiabatic_process,
            'output':'Adiabatic Process (w)',
            'formula':'w=(n*8.3(Ti-Tf))/Y-1'
        },
        'Isobaric Process':{
            'id':3,
            'form':forms.IsobaricProcessForm,
            'name':'Isobaric Process',
            'result':cal_Isobaric_process,
            'output':'Isobaric Process (W)',
            'formula':'W=P*dV'

        },
        'Second law of Thermodynamics':{
            'id':4,
            'form':forms.SecondlawofThermodynamicsForm,
            'name':'Second law of Thermodynamics',
            'result':cal_Second_law_of_Thermodynamics,
            'output':'Second law of Thermodynamics(dS)',
            'formula':'dS=dQ/T'
        },
    },
    'V-Belt Calculator':{
        'V-Belt Calculator':{
            'id':1,
            'form':forms.VBeltCalculatorForm,
            'name':'V-Belt calculator',
            'result':cal_V_Belt_Calculator,
            'output':'V-Belt calculator (vb)',
            'formula':'vb=3.142*(r1+r2)+2*3+(r1-r2)^2/d'
        },
    },
    'Storage Capacity Of Rectangular Tank':{
        'Storage Capacity Of Rectangular Tank':{
            'id':1,
            'form':forms.StorageCapacityOfRectangularTankForm,
            'name':'Storage Capacity of Rectangular Tank',
            'result':cal_Storage_Capacity_Of_Rectangular_Tank,
            'output':'Storage Capacity of Rectangular Tank (sc)',
            'formula':'sc=(l*w*h)/231'
        },
    },
    'Pipe Friction Loss':{
        'Pipe Friction Loss':{
            'id':1,
            'form':forms.PipeFrictionLossForm,
            'name':'Pipe Friction Loss',
            'result':cal_Pipe_friction_loss,
            'output':'Pipe Friction Loss (h1)',
            'formula':'h1=f*(L/D)*(V^2/2*g)'

        },
    },
    'Push And Pull Of Hydraulic':{
        'Push And Pull Of Hydraulic':{
            'id':1,
            'form':forms.PushnPullForm,
            'name':'Push and Pull Of Hydraulic',
            'result':push_and_pull_calc,
            'output':'Push & Pull of Hydraulic (lbs)',
            'formula':' Push = PSI*3.14*b^2/4 \n''Pull = PSI*3.14(b^2 - d^2)/4'
        },
    },
    'Pipe Enlargement Calculator':{
        'Pipe Enlargement Calculator':{
            'id':1,
            'form':forms.PipeEnlargementCalculatorForm,
            'name':'Pipe Enlargement calculator',
            'result':cal_pipe_enlargement,
            'output':'Pipe Enlargement Calculator (K)',
            'formula':'\n  K=2.6*sin(ϴ/2)*pow((1-β^2),2) if ϴ <= 45' '\n  K = pow((1-β^2),2) if(45<ϴ<=180)'
        },
    },
 }




def home_cards(request):
    template='home_card.html'
    context={}
    return render(request,'home_card.html',context)


def show_cards(request):
    cards = CARD_TO_FORMULA.keys()
    card_list = []
    for card in cards:
        card_dict = {}

        card_dict['name'] = card.lower().replace(' ', '_')

        card_list.append(card_dict)
    return render(request, 'show_cards.html', {'cards': card_list})


def detail(request, card_name):
    key_card_name = card_name.replace('_', ' ').title()
    details = CARD_TO_FORMULA.get(key_card_name)
    return render(request, 'card_detail.html', {'details': details, 'card_name': card_name})

def formula_page(request, card_name, detail):
    key_card_name = card_name.replace('_', ' ').title()
    DETAIL_DICT = CARD_TO_FORMULA.get(key_card_name).get(detail)
    formula = DETAIL_DICT.get('formula')
    name = DETAIL_DICT.get('name')
    description = DETAIL_DICT.get('description', '')
    if request.method == 'POST':
        Forms = DETAIL_DICT.get('form')
        form = Forms(request.POST)
        if form.is_valid():
             res = DETAIL_DICT.get('result')(form)
             output_text = DETAIL_DICT.get('output')
             if type(res) == dict:
                final_output = 'Push Force = {} \n Pull Force = {}'.format(res['push_r'], res['pull_r'])
             else:
                final_output = output_text + '= {}'.format(str(res))
             return render(request, 'formula_page.html', {'form': form,
                                                 'r': final_output,
                                                  'formula': formula,
                                                 'name': name,
                                                'description': description

                                                 })

    else:
        form = DETAIL_DICT.get('form')()
    return render(request, 'formula_page.html', {'form': form,
                                                 'formula': formula,
                                                 'name': name,
                                                 'description': description
                                                 })


