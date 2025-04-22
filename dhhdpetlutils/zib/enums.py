"""This module stores the Enum classes for the zib subproject"""

from dhhdpetlutils.core.enums import ExtendedStrEnum


class InputZibTemplateName(ExtendedStrEnum):
    """Enumerate the supported input template to run the ETL workflow"""

    PATIENT_2024 = "DataHub-Patient-2024"
    ALCOHOL_GEBRUIK_2017 = "DataHub-AlcoholGebruik-2017"
    ALCOHOL_GEBRUIK_2023 = "DataHub-AlcoholGebruik-2023"
    BURGERLIJKE_STAAT_2017 = "DataHub-BurgerlijkeStaat-2017"
    BURGERLIJKE_STAAT_2023 = "DataHub-BurgerlijkeStaat-2023"
    CONTACTPERSOON_2017 = "DataHub-Contactpersoon-2017"
    WOONSITUATIE_2017 = "DataHub-Woonsituatie-2017"
    VERMOGENTOTZICHWASSEN_2020 = "DataHub-VermogenTotZichWassen-2020"
    VERMOGENTOTZICHKLEDEN_2020 = "DataHub-VermogenTotZichKleden-2020"
    VERMOGENTOTUITERLIJKEVERZORGING_2020 = "DataHub-VermogenTotUiterlijkeVerzorging-2020"
    VERMOGENTOTZELFSTANDIGMEDICATIEGEBRUIK_2020 = "DataHub-VermogenTotZelfstandigMedicatiegebruik-2020"
    VERMOGENTOTETEN_2020 = "DataHub-VermogenTotEten-2020"
    VERMOGENTOTDRINKEN_2020 = "DataHub-VermogenTotDrinken-2020"
    VERMOGENTOTMONDVERZORGING_2020 = "DataHub-VermogenTotMondverzorging-2020"
    VERMOGENTOTTOILETGANG_2020 = "DataHub-VermogenTotToiletgang-2020"
    INFORMED_CONSENT = "DataHub-InformedConsent"
