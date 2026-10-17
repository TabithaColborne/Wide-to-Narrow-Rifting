# Generated from: 800C_EX1cmF.ipynb
# Converted at: 2026-07-13T09:26:00.212Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

#import tools
from underworld import UWGeodynamics as GEO
from underworld import visualisation as vis

#units system
u = GEO.u
#scale model
velocity = 1. * u.centimeter / u.year
model_length = 660e3 * u.meter
surfaceTemp = 293.15 * u.degK
baseModelTemp = 1603.15 * u.degK
bodyforce = 3300 * u.kilogram / u.metre**3 * 9.81 * u.meter / u.second**2

KL = model_length
Kt = KL / velocity
KM = bodyforce * KL**2 * Kt**2
KT = (baseModelTemp - surfaceTemp)

GEO.scaling_coefficients["[length]"] = KL
GEO.scaling_coefficients["[time]"] = Kt
GEO.scaling_coefficients["[mass]"]= KM
GEO.scaling_coefficients["[temperature]"] = KT

#define model
Model = GEO.Model(elementRes=(660, 200), 
                  minCoord=(0. * u.kilometer, -190. * u.kilometer), 
                  maxCoord=(660. * u.kilometer, 10. * u.kilometer), 
                  gravity=(0.0, -9.81 * u.meter / u.second**2))

Model.outputDir = "800C_EX1cm"

#add materials
Model.diffusivity = 9e-7 * u.metre**2 / u.second 
Model.capacity    = 1000. * u.joule / (u.kelvin * u.kilogram)
stickyAir = Model.add_material(name="StickyAir", shape=GEO.shapes.Layer(top=Model.top, bottom= 0.0 * u.kilometer))
Upper_Crust = Model.add_material(name="Upper_Crust", shape=GEO.shapes.Layer(top=stickyAir.bottom, bottom=-10 * u.kilometer))
Middle_Crust = Model.add_material(name="Irindina_Gneiss", shape=GEO.shapes.Layer(top=Upper_Crust.bottom, bottom=-20. * u.kilometer))
Lower_Crust = Model.add_material(name="Basement", shape=GEO.shapes.Layer(top=Middle_Crust.bottom, bottom=-40. * u.kilometer))
mantleLithosphere = Model.add_material(name="MantleLithosphere", shape=GEO.shapes.Layer(top=Lower_Crust.bottom, bottom=-100. * u.kilometer))
asthenosphere = Model.add_material(name="asthenosphere", shape = GEO.shapes.Layer(top= mantleLithosphere.bottom, bottom=Model.bottom))
sediment = Model.add_material(name="Sediment")

stickyAir.diffusivity = 1.0e-6 * u.metre**2 / u.second
stickyAir.capacity = 100. * u.joule / (u.kelvin * u.kilogram)

stickyAir.density = 1. * u.kilogram / u.metre**3
Upper_Crust.density = GEO.LinearDensity(2620. * u.kilogram / u.metre**3, thermalExpansivity=3e-5 / u.kelvin)
Middle_Crust.density = GEO.LinearDensity(2620. * u.kilogram / u.metre**3, thermalExpansivity=3e-5 / u.kelvin)
Lower_Crust.density = GEO.LinearDensity(2620. * u.kilogram / u.metre**3, thermalExpansivity=3e-5 / u.kelvin)
mantleLithosphere.density = GEO.LinearDensity(3300. * u.kilogram / u.metre**3, thermalExpansivity=3e-5 / u.kelvin)
asthenosphere.density = GEO.LinearDensity(3300. * u.kilogram / u.metre**3, thermalExpansivity=3e-5 / u.kelvin)
sediment.density = GEO.LinearDensity(reference_density=2300. * u.kilogram / u.metre**3)

Upper_Crust.radiogenicHeatProd = 1.15e-6 * u.watt / u.meter**3
Middle_Crust.radiogenicHeatProd = 1.15e-6 * u.watt / u.meter**3
Lower_Crust.radiogenicHeatProd = 1.15e-6 * u.watt / u.meter**3
sediment.radiogenicHeatProd = 1.15e-6 * u.microwatt / u.meter**3

#define viscosities
rh = GEO.ViscousCreepRegistry()
Model.minViscosity = 1e18 * u.pascal * u.second
Model.maxViscosity = 1e23 * u.pascal * u.second
stickyAir.viscosity = 1e18 * u.pascal * u.second
Upper_Crust.viscosity  = rh.Wet_Quartz_Dislocation_Gleason_and_Tullis_1995
Middle_Crust.viscosity = rh.Wet_Quartz_Dislocation_Gleason_and_Tullis_1995
Lower_Crust.viscosity = rh.Wet_Quartz_Dislocation_Gleason_and_Tullis_1995
mantleLithosphere.viscosity  = rh.Wet_Olivine_Dislocation_Hirth_and_Kohlstedt_2003
asthenosphere.viscosity = rh.Wet_Olivine_Dislocation_Hirth_and_Kohlstedt_2003
sediment.viscosity = rh.Wet_Quartz_Dislocation_Gleason_and_Tullis_1995

#define plasticity
pl = GEO.PlasticityRegistry()
Upper_Crust.plasticity= GEO.DruckerPrager(name="crust",
                                                cohesion=20. * u.megapascal,
                                                cohesionAfterSoftening=0.2 * u.megapascal,
                                                frictionCoefficient=0.577,
                                                frictionAfterSoftening=0.1154,
                                                epsilon1=0.0, epsilon2=0.15)
Middle_Crust.plasticity= GEO.DruckerPrager(name="crust",
                                                cohesion=20. * u.megapascal,
                                                cohesionAfterSoftening=0.2 * u.megapascal,
                                                frictionCoefficient=0.577,
                                                frictionAfterSoftening=0.1154,
                                                epsilon1=0.0, epsilon2=0.15)
Lower_Crust.plasticity= GEO.DruckerPrager(name="crust",
                                                cohesion=20. * u.megapascal,
                                                cohesionAfterSoftening=0.2 * u.megapascal,
                                                frictionCoefficient=0.577,
                                                frictionAfterSoftening=0.1154,
                                                epsilon1=0.0, epsilon2=0.15)
mantleLithosphere.plasticity= GEO.DruckerPrager(name="crust",
                                                cohesion=20. * u.megapascal,
                                                cohesionAfterSoftening=0.2 * u.megapascal,
                                                frictionCoefficient=0.577,
                                                frictionAfterSoftening=0.0577,
                                                epsilon1=0.0, epsilon2=0.15)
asthenosphere.plasticity = GEO.DruckerPrager(name="crust",
                                                cohesion=20. * u.megapascal,
                                                cohesionAfterSoftening=0.2 * u.megapascal,
                                                frictionCoefficient=0.577,
                                                frictionAfterSoftening=0.0577,
                                                epsilon1=0.0, epsilon2=0.15)
sediment.plasticity= GEO.DruckerPrager(name="crust",
                                                cohesion=20. * u.megapascal,
                                                cohesionAfterSoftening=0.2 * u.megapascal,
                                                frictionCoefficient=0.577,
                                                frictionAfterSoftening=0.1154,
                                                epsilon1=0.0, epsilon2=0.15)

#temperature boundary conditions

Model.set_heatFlowBCs(bottom=(0.027 * u.watt / u.metre**2, asthenosphere))

Model.set_temperatureBCs(top=293.15 * u.degK, nodeSets = [(stickyAir.shape, 293.15 * u.degK)])


#melt

#velocity boundary conditions
import underworld.function as fn

Model.set_velocityBCs(left=[-1. * u.centimeter / u.year, None],
                      right=[1. * u.centimeter / u.year, None],
                      bottom=GEO.LecodeIsostasy(reference_mat=asthenosphere, average =False))


#surface processes
import numpy as np

npoints = int(Model.length.magnitude)


coords = np.ndarray((npoints, 2))
coords[:, 0] = np.linspace(GEO.nd(Model.minCoord[0]), GEO.nd(Model.maxCoord[0]), npoints)
coords[:, 1] = GEO.nd(stickyAir.bottom)

Model.surfaceProcesses = GEO.surfaceProcesses.velocitySurface_2D(
    airIndex=stickyAir.index,
    sedimentIndex=sediment.index,
    sedimentationRate= 2.*u.millimeter / u.year,
    erosionRate= 2.*u.millimeter / u.year,
    surfaceElevation=stickyAir.bottom,
    surfaceArray = coords
)

def gaussian(xx, centre, width):
    return ( np.exp( -(xx - centre)**2/width))

maxDamage = 0.25
centre = (GEO.nd(330. * u.kilometer), GEO.nd(-40. * u.kilometer))
width = GEO.nd(75. * u.kilometer)  # this gives a normal distribution

Model.plasticStrain.data[:] = maxDamage * np.random.rand(*Model.plasticStrain.data.shape[:])
Model.plasticStrain.data[:,0] *= gaussian(Model.swarm.particleCoordinates.data[:,0], centre[0], width)
Model.plasticStrain.data[:,0] *= gaussian(Model.swarm.particleCoordinates.data[:,1], centre[1], width*100)

air_mask = Model.swarm.particleCoordinates.data[:,1] > GEO.nd(0 * u.kilometer)

Model.plasticStrain.data[air_mask] = 0.0

#passive tracers

#initialise model

Model.init_model()

Model.solver.set_inner_method("mumps")
Model.solver.set_penalty(1e6)

def post_hook():  
    
    coords = fn.input()
    zz = (coords[0] - GEO.nd(Model.minCoord[0])) / (GEO.nd(Model.maxCoord[0]) - GEO.nd(Model.minCoord[0]))
    fact = fn.math.pow(fn.math.tanh(zz*20.0) + fn.math.tanh((1.0-zz)*20.0) - fn.math.tanh(20.0), 4)
    Model.plasticStrain.data[:] = Model.plasticStrain.data[:] * fact.evaluate(Model.swarm)


#temperature boundary conditions
Model.set_temperatureBCs(top=293.15 * u.degK, 
                         bottom=1603.15 * u.degK, 
                         nodeSets = [(stickyAir.shape, 293.15 * u.degK), (asthenosphere.shape, 1603.15 * u.kelvin)])

solver = Model.solver

solver.set_inner_method("mumps")

solver.options.A11.ksp_rtol=1e-4
solver.options.A11.ksp_set_min_it_converge = 10
solver.options.A11.use_previous_guess = True
solver.options.scr.ksp_rtol=1e-6 #1e-3
solver.options.scr.use_previous_guess = True
solver.options.scr.ksp_set_min_it_converge = 10
solver.options.scr.ksp_type = "cg"

#solver.options.main.help = ""
solver.options.main.remove_constant_pressure_null_space=True
#solver.options.main.Q22_pc_type = "uwscale"
solver.set_penalty(1.0e2)
#Model.solver = solver
Model.run_for(40.0 * u.megayear, checkpoint_interval=100000 * u.year,restartStep=-1, restartDir="800C_EX1cm")