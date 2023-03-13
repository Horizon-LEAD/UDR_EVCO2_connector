"""Processing Module

vehicle_type_flag:
  0: Electric Super Soco CPX 12
  1: Electric VAN Maxus eDelivery 125cc
"""

from os.path import join

import pandas as pd


def run(udr_output: str, vehicle_type_flag: int, out_dir: str) -> None:
    """_summary_

    :param udr_output: The path to the xlsx file of the UDR output.
    :type udr_output: str
    :param vehicle_type_flag: A number that defines the vehicle type.
    :type vehicle_type_flag: int
    :param out_dir: The output directory.
    :type vehicle_type_flag: str
    :return: Does not return anything, creates and saves the output file.
    :rtype: None
    """
    df_udr = pd.read_excel(udr_output)
    df_cons = df_udr
    df_ev_cons = df_cons.drop(['energy_kWh', 'total_distance_km'], axis=1)
    # compute energy TJ
    # [29.44 - 31.06] kWh per 100km -> SONAE VAN
    # avg = 30.25
    a_van = 30.25
    # [0.67 - 1]kwh per 100km -> motorbike
    # avg = 0.33
    a_motor = 0.165

    coeff = a_van
    if vehicle_type_flag == 0:
        coeff = a_motor

    df_ev_cons['energy_TJ'] = (coeff/100) * df_udr['total_distance_km'] * pow(3.6, 10^(-6))

    # rename columns based on github repository
    # https://github.com/Horizon-LEAD/EV_EMISSIONS_UPM/blob/lead-packaging/src/evco2.R
    # Stock * energykwh
    d_f = df_ev_cons.rename(columns={"number_of_vehicles_used": "Stock", "energy_TJ": "energykwh"})

    # EV CONS
    # save to excel without index
    # rename columns (see modified code in github) - Stock * energykwh
    d_f.to_excel(join(out_dir, "EV_CONS.xlsx"), index=False)

    return d_f
