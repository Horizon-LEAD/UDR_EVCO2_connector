import pandas as pd
# inputs:
# UDR_outputs.xlsx
# vehicle_type_flag:
#   0 -> Electric Super Soco CPX 12
#   1 -> Electric VAN Maxus eDelivery 125cc

def udr_evco2_connector(df_UDR_output,vehicle_type_flag):

	df_udr = pd.read_excel('output.xlsx')

	df_cons = df_udr
	df_ev_cons = df_cons.drop(['energy_kWh','total_distance_km'], axis=1)

	# compute energy TJ
	# [29.44 - 31.06] kWh per 100km -> SONAE VAN
	# avg = 30.25
	a_van = 30.25
	# [0.67 - 1]kwh per 100km -> motorbike
	# avg = 0.33
	a_motor = 0.165
	vehicle_type_flag = 1

	if vehicle_type_flag == 1:
	    a = a_van
	elif vehicle_type_flag == 0:
	    a = a_motor
	df_ev_cons['energy_TJ'] = (a/100) * df_udr['total_distance_km'] * pow(3.6,10^(-6))

	# rename columns based on github repository 
	# https://github.com/Horizon-LEAD/EV_EMISSIONS_UPM/blob/lead-packaging/src/evco2.R
	# Stock * energykwh
	df = df_ev_cons.rename(columns={"number_of_vehicles_used": "Stock", "energy_TJ": "energykwh"})

	# EV CONS 
	# save to excel without index
	# rename columns (see modified code in github) - Stock * energykwh

	df.to_excel("EV_CONS.xlsx", index=False)

	return df


