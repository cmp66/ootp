import math
import sys

low_contact_modifiers = {
    "low_babip" : 0.6,
    "high_babip" : 0.7,
    "low_power" : 0.1,
    "high_power" : 0.2525,
    "low_avk" : 0.33,
    "high_avk" : 0.2

}

high_contact_modifiers = {
    "low_babip" : 1.3,
    "high_babip" : 0.8,
    "low_power" : 0.2,
    "high_power" : 0.44,
    "low_avk" : 0.7,
    "high_avk" : 0.45

}


def calculate_base_ratings(raw_contact, raw_power, raw_avk):
    calc_contact = (raw_contact-1)*2
    calc_power = (raw_power-1)*2
    calc_avk = (raw_avk-1)*2

    return calc_contact, calc_power, calc_avk

def calc_avk_power_adjustors(calc_contact, calc_power, calc_avk):
    modifiers = high_contact_modifiers if calc_contact > 100 else low_contact_modifiers
    
    if calc_avk > 100:
        if calc_power > 100:
            avk_power_adjustor_low_contact = low_contact_modifiers["high_avk"]*(calc_avk-100) + low_contact_modifiers["high_power"]*(calc_power-100)
            avk_power_adjustor_high_contact = high_contact_modifiers["high_avk"]*(calc_avk-100) + high_contact_modifiers["high_power"]*(calc_power-100)
        else:
            avk_power_adjustor_low_contact = low_contact_modifiers["high_avk"]*(calc_avk-100) + low_contact_modifiers["low_power"]*(calc_power-100)
            avk_power_adjustor_high_contact = high_contact_modifiers["high_avk"]*(calc_avk-100) + high_contact_modifiers["low_power"]*(calc_power-100)
    else:
        if calc_power > 100:
            avk_power_adjustor_low_contact = low_contact_modifiers["low_avk"]*(calc_avk-100) + low_contact_modifiers["high_power"]*(calc_power-100)
            avk_power_adjustor_high_contact = high_contact_modifiers["low_avk"]*(calc_avk-100) + high_contact_modifiers["high_power"]*(calc_power-100)
        else:
            avk_power_adjustor_low_contact = low_contact_modifiers["low_avk"]*(calc_avk-100) + low_contact_modifiers["low_power"]*(calc_power-100)
            avk_power_adjustor_high_contact = high_contact_modifiers["low_avk"]*(calc_avk-100) + high_contact_modifiers["low_power"]*(calc_power-100)
    

    return avk_power_adjustor_low_contact, avk_power_adjustor_high_contact
    
def round_up_to_even(f):
    return math.ceil(f / 2.) * 2

def calc_babip(raw_contact, raw_power, raw_avk):
    scaled = False
    local_contact, local_power, local_avk = raw_contact, raw_power, raw_avk
    if raw_contact < 11 and raw_power < 11 and raw_avk < 11:
        local_contact = local_contact * 10
        local_power = local_power * 10
        local_avk = local_avk * 10
        scaled = True
    
    calc_contact, calc_power, calc_avk = calculate_base_ratings(local_contact, local_power, local_avk)
    modifiers = low_contact_modifiers
    #print(f'calc contact:{calc_contact}  calc_power:{calc_power} calc_avk:{calc_avk}')

    avk_power_adjustor_low_contact, avk_power_adjustor_high_contact = calc_avk_power_adjustors(calc_contact, calc_power, calc_avk)
    #print(f'avk_power_adjustor_low_contact:{avk_power_adjustor_low_contact}  avk_power_adjustor_high_contact:{avk_power_adjustor_high_contact}')
    if calc_contact > 100:
        intermediate_contact = (calc_contact - 100 - avk_power_adjustor_high_contact)/high_contact_modifiers["low_babip"] + 100
    else:
        intermediate_contact = (calc_contact - 100 - avk_power_adjustor_low_contact)/low_contact_modifiers["low_babip"] + 100

    #print(f'intermediate_contact:{intermediate_contact}')

    if intermediate_contact > 100:
        if calc_contact > 100:
            calc_babip = (calc_contact - 100 - avk_power_adjustor_high_contact)/high_contact_modifiers["high_babip"] + 100
        else:
            calc_babip = (calc_contact - 100 - avk_power_adjustor_high_contact)/low_contact_modifiers["high_babip"] + 100
    else:
        if calc_contact > 100:
            calc_babip = (calc_contact - 100 - avk_power_adjustor_high_contact)/high_contact_modifiers["low_babip"] + 100
        else:
            calc_babip = (calc_contact - 100 - avk_power_adjustor_low_contact)/low_contact_modifiers["low_babip"] + 100
    
    final_babip = round_up_to_even( (round(calc_babip)+1)/2 )

    if scaled:
        final_babip = round(final_babip/10)

    return final_babip

if __name__ == '__main__':
    contact = int(sys.argv[1])
    power = int(sys.argv[2])
    avk = int(sys.argv[3])

    print (f'BABIP: {calc_babip(contact, power, avk)}')
