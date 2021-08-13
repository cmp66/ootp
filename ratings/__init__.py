from sqlalchemy.sql import base
from db import Player, PlayerBatting, PlayerFielding, PlayerPitching

####
# Adjustments to normalize ratings around a 6 as a BaseException
####
CATCHER_ADJUSTMENT = 0.2824
SHORTSTOP_ADJUSTMENT = 0.2450
SECONDBASE_ADJUSTMENT = 0.2836
THIRDBASE_ADJUSTMENT = 0.4089
FIRSTBASE_ADJUSTMENT = 3.030
LEFTFIELD_ADJUSTMENT = 0.4329
CENTERFIELD_ADJUSTMENT = 0.4140
RIGHTFIELD_ADJUSTMENT = 0.4115

BATTING_ADJUSTMENT = 0.1960
CATCHER_BATTING_ADJUSTMENT = 0.1754

###
#  Settings to provide ratios between offense and defese ratings
###
CATCHER_FIELD_ADJUST = 0.25
CATCHER_BATTING_ADJUST = 0.75
FIRSTBASE_FIELD_ADJUST = 0.10
FIRSTBASE_BATTING_ADJUST = 0.90
SECONDBASE_FIELD_ADJUST = 0.20
SECONDBASE_BATTING_ADJUST = 0.80
SHORTSTOP_FIELD_ADJUST = 0.30
SHORTSTOP_BATTING_ADJUST = 0.70
THIRDBASE_FIELD_ADJUST = 0.20
THIRDBASE_BATTING_ADJUST = 0.80
LEFTFIELD_FIELD_ADJUST = 0.15
LEFTFIELD_BATTING_ADJUST = 0.85
CENTERFIELD_FIELD_ADJUST = 0.30
CENTERFIELD_BATTING_ADJUST = 0.70
RIGHTFIELD_FIELD_ADJUST = 0.15
RIGHTFIELD_BATTING_ADJUST = 0.85

###
# Offsets to get 0 WAR rating at 100
###
### 2055
# CATCHER_NORMALIZATION = 17
# SHORTSTOP_NORMALIZATION = -2
# SECONDBASE_NORMALIZATION = 10
# THIRDBASE_NORMALIZATION = 8
# FIRSTBASE_NORMALIZATION = 2
# LEFTFIELD_NORMALIZATION = 7
# CENTERFIELD_NORMALIZATION = -10
# RIGHTFIELD_NORMALIZATION = 5
# DH_NORMALIZATION = 0

### 2056 PBL
CATCHER_NORMALIZATION = 16
SHORTSTOP_NORMALIZATION = -9
SECONDBASE_NORMALIZATION = 2
THIRDBASE_NORMALIZATION = -6
FIRSTBASE_NORMALIZATION = 1
LEFTFIELD_NORMALIZATION = 1
CENTERFIELD_NORMALIZATION = -5
RIGHTFIELD_NORMALIZATION = -2
DH_NORMALIZATION = 0

### Miami
# CATCHER_NORMALIZATION = 21
# SHORTSTOP_NORMALIZATION = 7
# SECONDBASE_NORMALIZATION = 12
# THIRDBASE_NORMALIZATION = 8
# FIRSTBASE_NORMALIZATION = 3
# LEFTFIELD_NORMALIZATION = 10
# CENTERFIELD_NORMALIZATION = 8
# RIGHTFIELD_NORMALIZATION = 10
# DH_NORMALIZATION = 0

### ABL
# CATCHER_NORMALIZATION = 19
# SHORTSTOP_NORMALIZATION = -5
# SECONDBASE_NORMALIZATION = 10
# THIRDBASE_NORMALIZATION = 4
# FIRSTBASE_NORMALIZATION = 9
# LEFTFIELD_NORMALIZATION = 9
# CENTERFIELD_NORMALIZATION = 0
# RIGHTFIELD_NORMALIZATION = 7
# DH_NORMALIZATION = 0


groundball_flyball_adjustment = {
    "EX FB": -4,
    "FB": -2,
    "NEU": 0,
    "GB": 2,
    "EX GB": 4,
}

####
# Pitching adjustments
###
BASE_PITCHING_ADJUSTMENT = 0.1035
SP_INDIVIDUAL_PITCHING_ADJUSTMENT = 0.2083
RP_INDIVIDUAL_PITCHING_ADJUSTMENT = 0.2083

SP_BASE_ADJUST = 0.85
SP_PITCH_ADJUST = 0.15


RP_BASE_ADJUST = 0.85
RP_PITCH_ADJUST = 0.15

### 2055
# SP_NORMALIZATION = 21
# RP_NORMALIZATION = 20

### 2056 PBL
CONTACT_PENALTY = 0
SP_NORMALIZATION = 24
RP_NORMALIZATION = 18

### miami
#SP_NORMALIZATION = 24
#RP_NORMALIZATION = 20

### ABL
#CONTACT_PENALTY = 0
#SP_NORMALIZATION = 33
#RP_NORMALIZATION = 30


class PlayerRatings:
    def calc_catcher_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.catcherability/scale  * 44.5 + fielding_ratings.catcherarm/scale  * 14.5
        ) * CATCHER_ADJUSTMENT

    def calc_shortstop_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.infieldrange/scale  * 50.5
            + fielding_ratings.infieldarm/scale  * 8
            + fielding_ratings.turndoubleplay/scale  * 8
            + fielding_ratings.infielderror/scale  * 7.5
        ) * SHORTSTOP_ADJUSTMENT

    def calc_secondbase_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.infieldrange * 40/scale 
            + fielding_ratings.infieldarm * 1.5/scale 
            + fielding_ratings.turndoubleplay * 9/scale 
            + fielding_ratings.infielderror * 8.25/scale 
        ) * SECONDBASE_ADJUSTMENT

    def calc_thirdbase_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.infieldrange/scale  * 16
            + fielding_ratings.infieldarm/scale  * 22
            + fielding_ratings.turndoubleplay/scale  * 0.25
            + fielding_ratings.infielderror/scale  * 7.5
        ) * THIRDBASE_ADJUSTMENT

    def calc_firstbase_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.infieldrange/scale  * 4
            + fielding_ratings.infieldarm/scale  * 0
            + fielding_ratings.turndoubleplay/scale  * 0
            + fielding_ratings.infielderror/scale  * 2
        ) * FIRSTBASE_ADJUSTMENT

    def calc_leftfield_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.outfieldrange/scale  * 33.5
            + fielding_ratings.outfieldarm/scale  * 3
            + fielding_ratings.outfielderror/scale  * 2
        ) * LEFTFIELD_ADJUSTMENT

    def calc_centerfield_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            fielding_ratings.outfieldrange/scale  * 35
            + fielding_ratings.outfieldarm/scale  * 1.75
            + fielding_ratings.outfielderror/scale  * 3.5
        ) * CENTERFIELD_ADJUSTMENT

    def calc_rightfield_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return (
            (fielding_ratings.outfieldrange/scale  * 25.5)
            + (fielding_ratings.outfieldarm/scale  * 14)
            + (fielding_ratings.outfielderror/scale  * 2)
        ) * RIGHTFIELD_ADJUSTMENT

    def calc_dh_defense_rating(self, fielding_ratings: PlayerFielding, scale: float) -> int:
        return 0.0

    fielding_calc = {
        "1B": calc_firstbase_defense_rating,
        "2B": calc_secondbase_defense_rating,
        "SS": calc_shortstop_defense_rating,
        "3B": calc_thirdbase_defense_rating,
        "C": calc_catcher_defense_rating,
        "LF": calc_leftfield_defense_rating,
        "CF": calc_centerfield_defense_rating,
        "RF": calc_rightfield_defense_rating,
        "DH": calc_dh_defense_rating,
    }

    def calculate_defense_rating(
        self, fielding_ratings: PlayerFielding, position: str, scale: float
    ) -> int:
        if position == "1B":
            rating = self.calc_firstbase_defense_rating(fielding_ratings, scale)
        elif position == "2B":
            rating = self.calc_secondbase_defense_rating(fielding_ratings, scale)
        elif position == "SS":
            rating = self.calc_shortstop_defense_rating(fielding_ratings, scale)
        elif position == "3B":
            rating = self.calc_thirdbase_defense_rating(fielding_ratings, scale)
        elif position == "LF":
            rating = self.calc_leftfield_defense_rating(fielding_ratings, scale)
        elif position == "CF":
            rating = self.calc_centerfield_defense_rating(fielding_ratings, scale)
        elif position == "RF":
            rating = self.calc_rightfield_defense_rating(fielding_ratings, scale)
        elif position == "C":
            rating = self.calc_catcher_defense_rating(fielding_ratings, scale)
        elif position == "DH":
            rating = self.calc_dh_defense_rating(fielding_ratings, scale)
        elif position in ["SP", "RP", "CL"]:
            rating = 0.0
        else:
            print(f"Invalid position {position}")
            rating = 0.0

        return int(round(rating))

    def get_base_batting_ratings_bytype(self, ratings: PlayerBatting, type: str):
        if type == "Overall":
            return ratings.contactrating, ratings.gaprating, ratings.powerrating, ratings.eyerating, ratings.krating
        elif type == "Potential":
            return ratings.contactpotential, ratings.gappotential, ratings.powerpotential, ratings.eyeprotential,  ratings.kprotential
        elif type == "vLeft":
            return ratings.babippotential, ratings.gapvleft, ratings.powervleft, ratings.eyevleft, ratings.kvleft
        elif type == "vRight":
            return ratings.babippotential, ratings.gapvright, ratings.powervright, ratings.eyevright, ratings.kvright

    def calculate_batting_rating(
        self, batting_ratings: PlayerBatting, position: str, type: str, scale: float
    ) -> int:
        if batting_ratings.battedballtype == "Flyball":
            type_adjustment = 3
        elif batting_ratings.battedballtype == "Groundball":
            type_adjustment = -3
        else:
            type_adjustment = 0

        input_contactrating, input_gaprating, input_powerrating, input_eyerating, input_krating =  self.get_base_batting_ratings_bytype(batting_ratings, type)
        if batting_ratings.contactpotential/scale < CONTACT_PENALTY:
            contactrating = input_contactrating/scale + (input_contactrating/scale-CONTACT_PENALTY) 
        else:
            contactrating = input_contactrating/scale
        if input_powerrating/scale  < 0:
            powerrating = input_powerrating/scale  + (input_powerrating/scale -6) 
        else:
            powerrating = input_powerrating/scale
        if input_eyerating/scale  < 0:
            eyerating = input_eyerating/scale  + (input_eyerating/scale -6)
        else:
            eyerating = input_eyerating/scale 
        if input_krating/scale  < CONTACT_PENALTY:
            krating = input_krating/scale  + (input_krating/scale-CONTACT_PENALTY)
        else:
            krating = input_krating/scale 
        if input_gaprating/scale  < 0:
            gaprating = input_gaprating/scale  + (input_gaprating/scale -6)
        else:
            gaprating = input_gaprating/scale 
        if position == "C":
            rating = (
                (contactrating * 21)
                + (gaprating * 5)
                + (powerrating * 17)
                + (eyerating * 17)
                + (krating * 21)
                #+ (batting_ratings.speedrating/scale * 15)
                + (type_adjustment * 4)
            ) * CATCHER_BATTING_ADJUSTMENT
        else:
            rating = (
                (contactrating * 21)
                + (gaprating * 5)
                + (powerrating * 17)
                + (eyerating * 17)
                + (krating * 21)
                + (type_adjustment * 4)
            ) * BATTING_ADJUSTMENT

        return int(round(rating))

    def calculate_overall_batter_rating(
        self,
        fielding_ratings: PlayerFielding,
        batting_ratings: PlayerBatting,
        position: str,
        type: str,
        scale: float
    ) -> int:
        brating = self.calculate_batting_rating(batting_ratings, position, type, scale)
        frating = self.calculate_defense_rating(fielding_ratings, position, scale)
        if position == "1B":
            rating = (
                brating * FIRSTBASE_BATTING_ADJUST + frating * FIRSTBASE_FIELD_ADJUST
            ) + FIRSTBASE_NORMALIZATION
        elif position == "2B":
            rating = (
                brating * SECONDBASE_BATTING_ADJUST + frating * SECONDBASE_FIELD_ADJUST
            ) + SECONDBASE_NORMALIZATION
        elif position == "SS":
            rating = (
                brating * SHORTSTOP_BATTING_ADJUST + frating * SHORTSTOP_FIELD_ADJUST
            ) + SHORTSTOP_NORMALIZATION
        elif position == "3B":
            rating = (
                brating * THIRDBASE_BATTING_ADJUST + frating * THIRDBASE_FIELD_ADJUST
            ) + THIRDBASE_NORMALIZATION
        elif position == "LF":
            rating = (
                brating * LEFTFIELD_BATTING_ADJUST + frating * LEFTFIELD_FIELD_ADJUST
            ) + LEFTFIELD_NORMALIZATION
        elif position == "CF":
            rating = (
                brating * CENTERFIELD_BATTING_ADJUST
                + frating * CENTERFIELD_FIELD_ADJUST
            ) + CENTERFIELD_NORMALIZATION
        elif position == "RF":
            rating = (
                brating * RIGHTFIELD_BATTING_ADJUST + frating * RIGHTFIELD_FIELD_ADJUST
            ) + RIGHTFIELD_NORMALIZATION
        elif position == "C":
            rating = (
                brating * CATCHER_BATTING_ADJUST + frating * CATCHER_FIELD_ADJUST
            ) + CATCHER_NORMALIZATION
        elif position == "DH":
            rating = brating + DH_NORMALIZATION
        elif position in ["CL", "SP", "RP"]:
            rating = 0.0
        else:
            print(f"Invalid position {position}")
            rating = 0.0

        return int(round(rating)), int(round(brating)), int(round(frating))

    def get_base_pitcher_ratings_bytype(self, ratings: PlayerPitching, type: str):
        if type == "Overall":
            return ratings.stuffrating, ratings.movementrating, ratings.controlrating
        elif type == "Potential":
            return ratings.stuffpotential, ratings.movementpotential, ratings.controlpotential
        elif type == "vLeft":
            return ratings.stuffvleft, ratings.movementvleft, ratings.controlvleft
        elif type == "vRight":
            return ratings.stuffvright, ratings.movementvright, ratings.controlvright

    def calculate_base_starting_pitching_rating(
        self, pitching_ratings: PlayerPitching, position: str, scale: float, type: str
    ) -> int:

        gb_fb_adjustment = groundball_flyball_adjustment.get(pitching_ratings.groundballflyball, 0)

        input_stuffrating, input_movementrating, input_controlrating = self.get_base_pitcher_ratings_bytype(pitching_ratings, type)

        adjusted_stuff_rating = input_stuffrating/scale
        adjusted_movement_rating =  input_movementrating/scale
        adjusted_control_rating =  input_controlrating/scale
        if adjusted_stuff_rating < 7:
            stuffrating = adjusted_stuff_rating + (adjusted_stuff_rating-7) 
        else:
            stuffrating = adjusted_stuff_rating
        if adjusted_movement_rating < 7:
            movementrating = adjusted_movement_rating + (adjusted_movement_rating-7) 
        else:
            movementrating = adjusted_movement_rating
        if adjusted_control_rating < 7:
            controlrating = adjusted_control_rating + (adjusted_control_rating-7)
        else:
            controlrating = adjusted_control_rating
        return (
            (gb_fb_adjustment * 0)
            + (stuffrating * 27)
            + (movementrating * 34)
            + (controlrating * 34)
            + (pitching_ratings.stamina/scale * 0)
            + (pitching_ratings.numpitches * 40)
        ) * BASE_PITCHING_ADJUSTMENT
 
    def calculate_base_relief_pitching_rating(
        self, pitching_ratings: PlayerPitching, position: str, scale: float, type: str
    ) -> int:

        gb_fb_adjustment = groundball_flyball_adjustment.get(pitching_ratings.groundballflyball, 0)

        input_stuffrating, input_movementrating, input_controlrating = self.get_base_pitcher_ratings_bytype(pitching_ratings, type)

        #print(f'stuff:{input_stuffrating}   movement:{input_movementrating}  control:{input_controlrating}')

        adjusted_stuff_rating = input_stuffrating/scale
        adjusted_movement_rating =  input_movementrating/scale
        adjusted_control_rating =  input_controlrating/scale
        
        if adjusted_stuff_rating < 6:
            stuffrating = adjusted_stuff_rating + (adjusted_stuff_rating-7) 
        else:
            stuffrating = adjusted_stuff_rating
        if adjusted_movement_rating < 8:
            movementrating = adjusted_movement_rating + (adjusted_movement_rating-7) 
        else:
            movementrating = adjusted_movement_rating
        if  adjusted_control_rating < 7:
            controlrating =  adjusted_control_rating + ( adjusted_control_rating-7)
        else:
            controlrating =  adjusted_control_rating
        return (
            (gb_fb_adjustment * 0)
            + (stuffrating * 40)
            + (movementrating * 55)
            + (controlrating * 26)
            + (pitching_ratings.stamina/scale * 0)
        ) * BASE_PITCHING_ADJUSTMENT

    def rating_ajust(self, rating, scale):
        return (rating)*(rating)/(10*scale)

    def get_pitching_ratings(self, pitching_ratings: PlayerPitching,  scale: float) -> [int]:
        pitches = []

        if pitching_ratings.fastballrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.fastballrating, scale))
        if pitching_ratings.changeuprating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.changeuprating, scale))
        if pitching_ratings.curveballrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.curveballrating, scale))
        if pitching_ratings.sliderrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.sliderrating*1.2, scale))
        if pitching_ratings.sinkerrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.sinkerrating, scale))
        if pitching_ratings.splitterrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.splitterrating, scale))
        if pitching_ratings.cutterrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.cutterrating, scale))
        if pitching_ratings.forkballrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.forkballrating, scale))
        if pitching_ratings.circlechangerating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.circlechangerating, scale))
        if pitching_ratings.screwballrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.screwballrating, scale))
        if pitching_ratings.knucklecurverating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.knucklecurverating*1.2, scale))
        if pitching_ratings.knuckleballrating > 0:
            pitches.append(self.rating_ajust(pitching_ratings.knuckleballrating*.12, scale))

        return pitches

    def get_pitching_potential_ratings(self, pitching_ratings: PlayerPitching, scale: float) -> [int]:
        pitches = []

        if pitching_ratings.fastballpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.fastballpotential, scale))
        if pitching_ratings.changeuppotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.changeuppotential, scale))
        if pitching_ratings.curveballpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.curveballpotential, scale))
        if pitching_ratings.sliderpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.sliderpotential, scale))
        if pitching_ratings.sinkerpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.sinkerpotential, scale))
        if pitching_ratings.splitterpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.splitterpotential, scale))
        if pitching_ratings.cutterpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.cutterpotential, scale))
        if pitching_ratings.forkballpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.forkballpotential, scale))
        if pitching_ratings.circlechangepotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.circlechangepotential, scale))
        if pitching_ratings.screwballpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.screwballpotential, scale))
        if pitching_ratings.knucklecurvepotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.knucklecurvepotential, scale))
        if pitching_ratings.knuckleballpotential > 0:
            pitches.append(self.rating_ajust(pitching_ratings.knuckleballpotential, scale))

        return pitches

    def calculate_individual_pitch_ratings(self, pitching_ratings, position, potential, scale):

        if potential:
            pitches = self.get_pitching_potential_ratings(pitching_ratings, scale)
        else:
            pitches = self.get_pitching_ratings(pitching_ratings, scale)
        pitches.sort(reverse=True)

        pitch1rating = pitches[0]/scale if len(pitches) > 0 else 0
        pitch2rating = pitches[1]/scale if len(pitches) > 1 else 0
        pitch3rating = pitches[2]/scale if len(pitches) > 2 else 0
        pitch4rating = pitches[3]/scale if len(pitches) > 3 else 0

        if position == "SP":
            return (
                (
                    (pitch1rating * 25)
                    + (pitch2rating * 25)
                    + (pitch3rating * 15)
                    + (pitch4rating * 15)
                    + (pitching_ratings.velocity - 90.0) * 0
                )
            ) * SP_INDIVIDUAL_PITCHING_ADJUSTMENT
        else:
            return (
                (
                    (pitch1rating * 45)
                    + (pitch2rating * 35)
                    + (pitching_ratings.velocity - 90.0) * 0
                )
            ) * RP_INDIVIDUAL_PITCHING_ADJUSTMENT

    def calculate_starter_pitcher_rating(self, pitching_ratings, position, type, scale):
        if pitching_ratings.numpitches < 3:
            return 0, 0, 0

        baserating = self.calculate_base_starting_pitching_rating(
            pitching_ratings, position, scale, type
        )

        if type == "Potential":
            indiv_rating = self.calculate_individual_pitch_ratings(
                pitching_ratings, position, True, scale
            )
        else:
            indiv_rating = self.calculate_individual_pitch_ratings(
                pitching_ratings, position, False, scale
            )

        rating = (
            (baserating * SP_BASE_ADJUST)
            + (indiv_rating * SP_PITCH_ADJUST)
            + SP_NORMALIZATION
        )

        return int(round(rating)), int(round(baserating)), int(round(indiv_rating))

    def calculate_relief_pitcher_rating(self, pitching_ratings, position, type, scale):
        
        baserating = self.calculate_base_relief_pitching_rating(
            pitching_ratings, position, scale, type
        )

        if type == "Potential":
            indiv_rating = self.calculate_individual_pitch_ratings(
                pitching_ratings, position, True, scale
            )
        else:
            indiv_rating = self.calculate_individual_pitch_ratings(
                pitching_ratings, position, False, scale
            )

        rating = (
            (baserating * RP_BASE_ADJUST)
            + (indiv_rating * RP_PITCH_ADJUST)
            + RP_NORMALIZATION
        )

        #print (f'type: {type}  scale:{scale} baserating:{baserating}  indiv_rating:{indiv_rating} ratings:{pitching_ratings}')

        return int(round(rating)), int(round(baserating)), int(round(indiv_rating))
