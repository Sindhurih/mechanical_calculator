from django import forms

class CylinderVelocityForm(forms.Form):
    flow_rate = forms.FloatField(label='Flow Rate')
    area = forms.FloatField(label='Area')


class CylinderVolumeCapacityForm(forms.Form):
    area = forms.FloatField(label='Area')
    stroke = forms.FloatField(label='Stroke')

class CylinderFlowRateForm(forms.Form):
    velocity = forms.FloatField(label='velocity')
    area = forms.FloatField(label='Area')

class CylinderFluidMotorTorqueForm(forms.Form):
    pressure = forms.FloatField(label='pressure')
    displacement=forms.FloatField(label='Displacement')

class CylinderFluidMotorSpeedForm(forms.Form):
    flow_rate = forms.FloatField(label='flow_rate')
    displacement=forms.FloatField(label='Displacement')



class FluidMotorPowerForm(forms.Form):
    torque = forms.FloatField(label='Torque')
    RPM = forms.FloatField(label='Revolutions per minute')


class BearingLengthForm(forms.Form):
    load = forms.FloatField(label='Bearing Load')
    pressure = forms.FloatField(label='Allowable pressure')
    diameter = forms.FloatField(label='Diameter')

class BearingHeatGenerationForm(forms.Form):
    friction=forms.FloatField(label='Bearing friction')
    load = forms.FloatField(label='Bearing Load')
    diameter = forms.FloatField (label='Diameter')
    RPM = forms.FloatField (label='Revolutions per minute')

class BearingWallAreaForm(forms.Form):
    factor=forms.FloatField(label='Factor')
    length=forms.FloatField(label='Length')
    diameter = forms.FloatField (label='Diameter')

class BearingLifeInRevolutionForm(forms.Form):
    dynamic_capacity=forms.FloatField(label='Dynamic Capacity (lbs)')
    radial_load=forms.FloatField(label='Applied radial load (lbs)')

class BearingHeatDissipationForm(forms.Form):
    Wall_area=forms.FloatField(label='Wall Area (cm^2)')
    bearing_temperature=forms.FloatField(label='Bearing Temperature (K)')
    outside_temperature=forms.FloatField(label='Outside Temperature (K)')

class BearingFluidMotorPowerForm(forms.Form):
    torque=forms.FloatField(label='Torque')
    rpm=forms.FloatField(label='RPM')

class FluidPressureForm(forms.Form):
    force=forms.FloatField(label='Force (lbs)')
    area=forms.FloatField(label='Unit area (in^2)')

class FluidPowerForm(forms.Form):
    pressure=forms.FloatField(label='Pressure (psi)')
    flow=forms.FloatField(label='Flow (GPM)')

class CompressibilityOfaFluidForm(forms.Form):
    bulk_modulus=forms.FloatField(label='Bulk Modulus ')

class SpecificGravityofFluidForm(forms.Form):
    weight=forms.FloatField(label='Weight')

class HydraulicHorsepowerForm(forms.Form):
    pressure = forms.FloatField(label='Pressure (psi)')
    oil_flow = forms.FloatField(label='Oil Flow (GPM)')

class HeatEquivalentOfFluidpowerForm(forms.Form):
    pressure = forms.FloatField(label='Pressure (psi)')
    oil_flow = forms.FloatField(label='Oil Flow (GPM)')

class StorageCapacityOfCylindricalTankForm(forms.Form):
    length = forms.FloatField (label='Length')
    diameter = forms.FloatField (label='Diameter')

class FirstLawOfThermodynamicsForm(forms.Form):
    u=forms.FloatField(label='Change in Internal Energy (⍙u)')
    w=forms.FloatField(label='Work Done (w)')

class AdiabaticProcessForm(forms.Form):
    n=forms.FloatField(label='No. of Moles')
    Ti=forms.FloatField(label='Initial Temperature (Ti)')
    Tf=forms.FloatField(label='Final Temperature (Tf)')
    Y=forms.FloatField(label='Ratio of specific Heat')

class IsobaricProcessForm(forms.Form):
    P=forms.FloatField(label='Constant pressure (Pa)')
    V=forms.FloatField(label='Change in volume (m^3)')

class SecondlawofThermodynamicsForm(forms.Form):
    dQ=forms.FloatField(label='Heat supplied to the system (J)')
    T=forms.FloatField(label='Absolute Temperature (K)')


class VBeltCalculatorForm(forms.Form):
    r1=forms.FloatField(label='First radius of pulley (r1)')
    r2=forms.FloatField(label='Second radius of pulley (r2)')
    d=forms.FloatField(label='distance (d)')

class StorageCapacityOfRectangularTankForm(forms.Form):
    l=forms.FloatField(label='Length of Reactangular Tank (l)')
    w=forms.FloatField(label='Width of Rectangular Tank (w)')
    h=forms.FloatField(label='Height of Rectangular Tank (h)')


class PipeFrictionLossForm(forms.Form):
    f=forms.FloatField(label='Friction Loss (f)')
    L=forms.FloatField(label='Length of a pipe (L)')
    D=forms.FloatField(label='Diameter of the pipe (D)')
    V=forms.FloatField(label='Flow rate (V)')
    g=forms.FloatField(label='Gravitational const')


class PushnPullForm(forms.Form):
    bore = forms.FloatField(label='Bore Diameter (inches)')
    pressure = forms.FloatField(label='Pressure (psi)')
    diameter = forms.FloatField(label='Rod Diameter (inches)')

class PipeEnlargementCalculatorForm(forms.Form):
    t=forms.IntegerField(label='Angle of Approach')
    B=forms.IntegerField(label='d minor/ d major')