# TODO: figure out imports

import clearwater_modules.shared.processes as shared_processes
from clearwater_modules import base
from clearwater_modules.nsm1.carbon.model import CarbonBudget
from clearwater_modules.nsm1.carbon import processes


@base.register_variable(models=CarbonBudget)
class Variable(base.Variable):
    ...

Variable(
    name='kpoc_tc',
    long_name='Temperature adjusted POC hydrolysis rate',
    units='1/d',
    description='Temperature adjusted POC hydrolysis rate',
    use='dynamic',
    process=processes.kpoc_tc,
)

Variable(
    name='POC_settling',
    long_name='POC concentration removed from cell due to settling',
    units='mg/L/d',
    description='POC concentration removed from cell due to settling',
    use='dynamic',
    process=processes.POC_settling,
)

Variable(
    name='POC_hydrolysis',
    long_name='POC concentration removed from cell due to hydrolysis',
    units='mg/L/d',
    description='POC concentration removed from cell due to hydrolysis',
    use='dynamic',
    process=processes.POC_hydrolysis,
)

Variable(
    name='POC_algal_mortality',
    long_name='POC concentration added to cell due to algal mortality',
    units='mg/L/d',
    description='POC concentration added to cell due to algal mortality',
    use='dynamic',
    process=processes.POC_algal_mortality,
)

Variable(
    name='POC_benthic_algae_mortality',
    long_name='POC concentration added to cell due to benthic algae mortality',
    units='mg/L/d',
    description='POC concentration added to cell due to benthic algae mortality',
    use='dynamic',
    process=processes.POC_benthic_algae_mortality,
)

Variable(
    name='dPOCdt',
    long_name='POC concentration change per timestep',
    units='mg/L/d',
    description='POC concentration change per timestep',
    use='dynamic',
    process=processes.dPOCdt
)

Variable(
    name='kdoc_tc',
    long_name='Dissolved organic carbon oxidation rate adjusted for temperature',
    units='1/d',
    description='Dissolved organic carbon oxidation rate adjusted for temperature',
    use='dynamic',
    process=processes.kdoc_tc
)

Variable(
    name='DOC_algal_mortality',
    long_name='DOC concentration added to cell due to algal mortality',
    units='mg/L/d',
    description='DOC concentration added to cell due to algal mortality',
    use='dynamic',
    process=processes.DOC_algal_mortality
)

Variable(
    name='DOC_benthic_algae_mortality',
    long_name='DOC concentration added to cell due to benthic algae mortality',
    units='mg/L/d',
    description='DOC concentration added to cell due to benthic algae mortality',
    use='dynamic',
    process=processes.DOC_benthic_algae_mortality,
)

Variable(
    name='DOC_oxidation',
    long_name='DOC concentration lost to cell due to oxidation',
    units='mg/L/d',
    description='DOC concentration lost to cell due to oxidation',
    use='dynamic',
    process=processes.DOC_oxidation
)

Variable(
    name='dDOCdt',
    long_name='DOC concentration change per timestep',
    units='mg/L/d',
    description='DOC concentration change per timestep',
    use='dynamic',
    process=processes.dDOCdt
)

Variable(
    name='K_H',
    long_name='Henrys coefficient',
    units='mol/L-atm',
    description='Henrys coefficient controlling the relative proportion of gaseous and aqueous phase CO2',
    use='dynamic',
    process=processes.Henrys_k
)

Variable(
    name='kac_tc',
    long_name='temperature dependent CO2 reaeration rate',
    units='1/d',
    description='temperature dependent CO2 reaeration rate',
    use='dynamic',
    process=processes.kac_tc
)

Variable(
    name='Atm_CO2_reaeration',
    long_name='Atmospheric CO2 reaeration',
    units='mg/L/d',
    description='Amount of DIC concentration change due to atmospheric exchange',
    use='dynamic',
    process=processes.Atmospheric_CO2_reaeration
)

Variable(
    name='DIC_algal_respiration',
    long_name='DIC generated by algal respiration',
    units='mg/L/d',
    description='DIC generated by algal respiration',
    use='dynamic',
    process=processes.DIC_algal_respiration
)

Variable(
    name='DIC_algal_photosynthesis',
    long_name='DIC consumed by algal photosynthesis',
    units='mg/L/d',
    description='DIC consumed by algal photosynthesis',
    use='dynamic',
    process=processes.DIC_algal_photosynthesis
)

Variable(
    name='DIC_benthic_algae_respiration',
    long_name='DIC generated by benthic algae respiration',
    units='mg/L/d',
    description='DIC generated by benthic algae respiration',
    use='dynamic',
    process=processes.DIC_benthic_algae_respiration
)

Variable(
    name='DIC_benthic_algae_photosynthesis',
    long_name='DIC consumed by benthic algae photosynthesis',
    units='mg/L/d',
    description='DIC consumed by benthic algae photosynthesis',
    use='dynamic',
    process=processes.DIC_benthic_algae_photosynthesis
)

Variable(
    name='DIC_CBOD_oxidation',
    long_name='DIC concentration change due to CBOD oxidation',
    units='mg/L/d',
    description='DIC concentration change due to CBOD oxidation',
    use='dynamic',
    process=processes.DIC_CBOD_oxidation
)

Variable(
    name='DIC_sed_release',
    long_name='DIC concentration change due to sediment release',
    units='mg/L/d',
    description='DIC concentration change due to sediment release',
    use='dynamic',
    process=processes.DIC_sed_release
)

Variable(
    name='dDICdt',
    long_name='DIC concentration change per timestep',
    units='mg/L/d',
    description='DIC concentration change per timestep',
    use='dynamic',
    process=processes.dDICdt
)

Variable(
    name='kah_tc',
    long_name='re-aeration rate temperature corrected (diffusion from atomsphere)',
    units='1/d',
    description='re-aeration rate temperature corrected(diffusion from atomsphere)',
    use='dynamic',
    process=processes.kah_tc
)
Variable(
    name='kaw_tc',
    long_name='wind derived re-aeration transfer velocity temperature corrected',
    units='m/d',
    description='wind derived re-aeration transfer velocity temperature corrected',
    use='dynamic',
    process=processes.kaw_tc
)