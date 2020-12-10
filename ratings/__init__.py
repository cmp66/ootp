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
THIRDBASE_FIELD_ADJUST = 0.15
THIRDBASE_BATTING_ADJUST = 0.85
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

### 2056
CATCHER_NORMALIZATION = 18
SHORTSTOP_NORMALIZATION = 7
SECONDBASE_NORMALIZATION = 12
THIRDBASE_NORMALIZATION = 6
FIRSTBASE_NORMALIZATION = 12
LEFTFIELD_NORMALIZATION = 10
CENTERFIELD_NORMALIZATION = 3
RIGHTFIELD_NORMALIZATION = 6
DH_NORMALIZATION = 0


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

SP_BASE_ADJUST = 0.90
SP_PITCH_ADJUST = 0.10


RP_BASE_ADJUST = 0.90
RP_PITCH_ADJUST = 0.10

### 2055
# SP_NORMALIZATION = 21
# RP_NORMALIZATION = 20

### 2056
SP_NORMALIZATION = 23
RP_NORMALIZATION = 6


class PlayerRatings:
    def calc_catcher_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.catcherability * 34.5 + fielding_ratings.catcherarm * 24.5
        ) * CATCHER_ADJUSTMENT

    def calc_shortstop_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.infieldrange * 50.5
            + fielding_ratings.infieldarm * 2
            + fielding_ratings.turndoubleplay * 8
            + fielding_ratings.infielderror * 7.5
        ) * SHORTSTOP_ADJUSTMENT

    def calc_secondbase_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.infieldrange * 40
            + fielding_ratings.infieldarm * 1.5
            + fielding_ratings.turndoubleplay * 9
            + fielding_ratings.infielderror * 8.25
        ) * SECONDBASE_ADJUSTMENT

    def calc_thirdbase_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.infieldrange * 13
            + fielding_ratings.infieldarm * 22
            + fielding_ratings.turndoubleplay * 3.25
            + fielding_ratings.infielderror * 7.5
        ) * THIRDBASE_ADJUSTMENT

    def calc_firstbase_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.infieldrange * 2
            + fielding_ratings.infieldarm * 0.75
            + fielding_ratings.turndoubleplay * 0.75
            + fielding_ratings.infielderror * 2
        ) * FIRSTBASE_ADJUSTMENT

    def calc_leftfield_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.outfieldrange * 33.5
            + fielding_ratings.outfieldarm * 3
            + fielding_ratings.outfielderror * 2
        ) * LEFTFIELD_ADJUSTMENT

    def calc_centerfield_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            fielding_ratings.outfieldrange * 35
            + fielding_ratings.outfieldarm * 1.75
            + fielding_ratings.outfielderror * 3.5
        ) * CENTERFIELD_ADJUSTMENT

    def calc_rightfield_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return (
            (fielding_ratings.outfieldrange * 25.5)
            + (fielding_ratings.outfieldarm * 14)
            + (fielding_ratings.outfielderror * 2)
        ) * RIGHTFIELD_ADJUSTMENT

    def calc_dh_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
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
        self, fielding_ratings: PlayerFielding, position: str
    ) -> int:
        if position == "1B":
            rating = self.calc_firstbase_defense_rating(fielding_ratings)
        elif position == "2B":
            rating = self.calc_secondbase_defense_rating(fielding_ratings)
        elif position == "SS":
            rating = self.calc_shortstop_defense_rating(fielding_ratings)
        elif position == "3B":
            rating = self.calc_thirdbase_defense_rating(fielding_ratings)
        elif position == "LF":
            rating = self.calc_leftfield_defense_rating(fielding_ratings)
        elif position == "CF":
            rating = self.calc_centerfield_defense_rating(fielding_ratings)
        elif position == "RF":
            rating = self.calc_rightfield_defense_rating(fielding_ratings)
        elif position == "C":
            rating = self.calc_catcher_defense_rating(fielding_ratings)
        elif position == "DH":
            rating = self.calc_dh_defense_rating(fielding_ratings)
        elif position in ["SP", "RP", "CL"]:
            rating = 0.0
        else:
            print(f"Invalid position {position}")
            rating = 0.0

        return int(round(rating))

    def calculate_batting_rating(
        self, batting_ratings: PlayerBatting, position: str, potential: bool
    ) -> int:
        if batting_ratings.battedballtype == "Flyball":
            type_adjustment = 3
        elif batting_ratings.battedballtype == "Groundball":
            type_adjustment = -3
        else:
            type_adjustment = 0

        if potential:
            if batting_ratings.contactpotential < 6:
                contactrating = batting_ratings.contactpotential + (batting_ratings.contactpotential-6) 
            else:
                contactrating = batting_ratings.contactpotential
            if batting_ratings.powerpotential < 0:
                powerrating = batting_ratings.powerpotential + (batting_ratings.powerpotential-6) 
            else:
                powerrating = batting_ratings.powerpotential
            if batting_ratings.eyepotential < 0:
                eyerating = batting_ratings.eyepotential + (batting_ratings.eyepotential-6)
            else:
                eyerating = batting_ratings.eyepotential
            if batting_ratings.kpotential < 6:
                krating = batting_ratings.kpotential + (batting_ratings.kpotential-6)
            else:
                krating = batting_ratings.kpotential
            if batting_ratings.gappotential < 0:
                gaprating = batting_ratings.gappotential + (batting_ratings.gappotential-6)
            else:
                gaprating = batting_ratings.gappotential
            if position == "C":
                contactrating = batting_ratings.contactpotential + (batting_ratings.contactpotential-6)
                powerrating = batting_ratings.pwerpotential + (batting_ratings.powerpotential-6) 
                eyerating = batting_ratings.eyepotential + (batting_ratings.eyepotential-6)
                krating = batting_ratings.kpotential + (batting_ratings.kpotential-6)
                gaprating = batting_ratings.gappotential + (batting_ratings.gappotential-6) 
                rating = (
                    (contactrating * 18)
                    + (gaprating * 9)
                    + (powerrating * 18)
                    + (eyerating * 18)
                    + (krating * 18)
                    + (batting_ratings.speedrating * 15)
                    + (type_adjustment * 4)
                ) * CATCHER_BATTING_ADJUSTMENT
            else:
                rating = (
                    (contactrating * 18)
                    + (gaprating * 9)
                    + (powerrating * 18)
                    + (eyerating * 18)
                    + (krating * 18)
                    + (type_adjustment * 4)
                ) * BATTING_ADJUSTMENT
        else:
            if batting_ratings.contactrating < 6:
                contactrating = batting_ratings.contactrating + (batting_ratings.contactrating-6) 
            else:
                contactrating = batting_ratings.contactrating
            if batting_ratings.powerrating < 0:
                powerrating = batting_ratings.powerrating + (batting_ratings.powerrating-6) 
            else:
                powerrating = batting_ratings.powerrating
            if batting_ratings.eyerating < 0:
                eyerating = batting_ratings.eyerating + (batting_ratings.eyerating-6)
            else:
                eyerating = batting_ratings.eyerating
            if batting_ratings.krating < 6:
                krating = batting_ratings.krating + (batting_ratings.krating-6)
            else:
                krating = batting_ratings.krating
            if batting_ratings.gaprating < 0:
                gaprating = batting_ratings.gaprating + (batting_ratings.gaprating-6)
            else:
                gaprating = batting_ratings.gaprating
            if position == "C":
                rating = (
                    (contactrating * 19)
                    + (gaprating * 5)
                    + (powerrating * 19)
                    + (eyerating * 19)
                    + (krating * 19)
                    + (batting_ratings.speedrating * 15)
                    + (type_adjustment * 4)
                ) * CATCHER_BATTING_ADJUSTMENT
            else:
                rating = (
                    (contactrating * 19)
                    + (gaprating * 5)
                    + (powerrating * 19)
                    + (eyerating * 19)
                    + (krating * 19)
                    + (type_adjustment * 4)
                ) * BATTING_ADJUSTMENT

        return int(round(rating))

    def calculate_overall_batter_rating(
        self,
        fielding_ratings: PlayerFielding,
        batting_ratings: PlayerBatting,
        position: str,
        potential: bool,
    ) -> int:
        brating = self.calculate_batting_rating(batting_ratings, position, potential)
        frating = self.calculate_defense_rating(fielding_ratings, position)
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

    def calculate_base_starting_pitching_rating(
        self, pitching_ratings: PlayerPitching, position: str, potential: bool
    ) -> int:

        gb_fb_adjustment = groundball_flyball_adjustment[
            pitching_ratings.groundballflyball
        ]

        if potential is False:
            if pitching_ratings.stuffrating < 6:
                stuffrating = pitching_ratings.stuffrating + (pitching_ratings.stuffrating-6) 
            else:
                stuffrating = pitching_ratings.stuffrating
            if pitching_ratings.movementrating < 6:
                movementrating = pitching_ratings.movementrating + (pitching_ratings.movementrating-6) 
            else:
                movementrating = pitching_ratings.movementrating
            if pitching_ratings.controlrating < 0:
                controlrating = pitching_ratings.controlrating + (pitching_ratings.controlrating-6)
            else:
                controlrating = pitching_ratings.controlrating
            return (
                (gb_fb_adjustment * 10)
                + (stuffrating * 34)
                + (movementrating * 31)
                + (controlrating * 31)
                + (pitching_ratings.stamina * 10)
                + (pitching_ratings.numpitches * 20)
            ) * BASE_PITCHING_ADJUSTMENT
        else:
            if pitching_ratings.stuffpotential < 6:
                stuffrating = pitching_ratings.stuffpotential + (pitching_ratings.stuffpotential-6) 
            else:
                stuffrating = pitching_ratings.stuffpotential
            if pitching_ratings.movementpotential < 6:
                movementrating = pitching_ratings.movementpotential + (pitching_ratings.movementpotential-6) 
            else:
                movementrating = pitching_ratings.movementpotential
            if pitching_ratings.controlpotential < 0:
                controlrating = pitching_ratings.controlpotential + (pitching_ratings.controlpotential-6)
            else:
                controlrating = pitching_ratings.controlpotential
            return (
                (gb_fb_adjustment * 10)
                + (stuffrating * 34)
                + (movementrating * 31)
                + (controlrating * 31)
                + (pitching_ratings.stamina * 10)
                + (pitching_ratings.numpitches * 20)
            ) * BASE_PITCHING_ADJUSTMENT

    def calculate_base_relief_pitching_rating(
        self, pitching_ratings: PlayerPitching, position: str, potential: bool
    ) -> int:

        gb_fb_adjustment = groundball_flyball_adjustment[
            pitching_ratings.groundballflyball
        ]

        if potential is False:
            if pitching_ratings.stuffrating < 11:
                stuffrating = pitching_ratings.stuffrating + (pitching_ratings.stuffrating-6) 
            else:
                stuffrating = pitching_ratings.stuffrating
            if pitching_ratings.movementrating < 11:
                movementrating = pitching_ratings.movementrating + (pitching_ratings.movementrating-6) 
            else:
                movementrating = pitching_ratings.movementrating
            if pitching_ratings.controlrating < 0:
                controlrating = pitching_ratings.controlrating + (pitching_ratings.controlrating-6)
            else:
                controlrating = pitching_ratings.controlrating
            return (
                (gb_fb_adjustment * 15)
                + (stuffrating * 45)
                + (movementrating * 45)
                + (controlrating * 26)
                + (pitching_ratings.stamina * 0)
            ) * BASE_PITCHING_ADJUSTMENT
        else:
            if pitching_ratings.stuffpotential < 6:
                stuffrating = pitching_ratings.stuffpotential + (pitching_ratings.stuffpotential-6) 
            else:
                stuffrating = pitching_ratings.stuffpotential
            if pitching_ratings.movementpotential < 6:
                movementrating = pitching_ratings.movementpotential + (pitching_ratings.movementpotential-6) 
            else:
                movementrating = pitching_ratings.movementpotential
            if pitching_ratings.controlpotential < 0:
                controlrating = pitching_ratings.controlpotential + (pitching_ratings.controlpotential-6)
            else:
                controlrating = pitching_ratings.controlpotential
            return (
                (gb_fb_adjustment * 15)
                + (stuffrating * 45)
                + (movementrating * 45)
                + (controlrating * 26)
                + (pitching_ratings.stamina * 0)
            ) * BASE_PITCHING_ADJUSTMENT

    def get_pitching_ratings(self, pitching_ratings: PlayerPitching) -> [int]:
        pitches = []

        if pitching_ratings.fastballrating > 0:
            pitches.append(pitching_ratings.fastballrating)
        if pitching_ratings.changeuprating > 0:
            pitches.append(pitching_ratings.changeuprating)
        if pitching_ratings.curveballrating > 0:
            pitches.append(pitching_ratings.curveballrating)
        if pitching_ratings.sliderrating > 0:
            pitches.append(pitching_ratings.sliderrating)
        if pitching_ratings.sinkerrating > 0:
            pitches.append(pitching_ratings.sinkerrating)
        if pitching_ratings.splitterrating > 0:
            pitches.append(pitching_ratings.splitterrating)
        if pitching_ratings.cutterrating > 0:
            pitches.append(pitching_ratings.cutterrating)
        if pitching_ratings.forkballrating > 0:
            pitches.append(pitching_ratings.forkballrating)
        if pitching_ratings.circlechangerating > 0:
            pitches.append(pitching_ratings.circlechangerating)
        if pitching_ratings.screwballrating > 0:
            pitches.append(pitching_ratings.screwballrating)
        if pitching_ratings.knucklecurverating > 0:
            pitches.append(pitching_ratings.knucklecurverating)
        if pitching_ratings.knuckleballrating > 0:
            pitches.append(pitching_ratings.knuckleballrating)

        return pitches

    def get_pitching_potential_ratings(self, pitching_ratings: PlayerPitching) -> [int]:
        pitches = []

        if pitching_ratings.fastballpotential > 0:
            pitches.append(pitching_ratings.fastballpotential)
        if pitching_ratings.changeuppotential > 0:
            pitches.append(pitching_ratings.changeuppotential)
        if pitching_ratings.curveballpotential > 0:
            pitches.append(pitching_ratings.curveballpotential)
        if pitching_ratings.sliderpotential > 0:
            pitches.append(pitching_ratings.sliderpotential)
        if pitching_ratings.sinkerpotential > 0:
            pitches.append(pitching_ratings.sinkerpotential)
        if pitching_ratings.splitterpotential > 0:
            pitches.append(pitching_ratings.splitterpotential)
        if pitching_ratings.cutterpotential > 0:
            pitches.append(pitching_ratings.cutterpotential)
        if pitching_ratings.forkballpotential > 0:
            pitches.append(pitching_ratings.forkballpotential)
        if pitching_ratings.circlechangepotential > 0:
            pitches.append(pitching_ratings.circlechangepotential)
        if pitching_ratings.screwballpotential > 0:
            pitches.append(pitching_ratings.screwballpotential)
        if pitching_ratings.knucklecurvepotential > 0:
            pitches.append(pitching_ratings.knucklecurvepotential)
        if pitching_ratings.knuckleballpotential > 0:
            pitches.append(pitching_ratings.knuckleballpotential)

        return pitches

    def calculate_individual_pitch_ratings(self, pitching_ratings, position, potential):

        if potential:
            pitches = self.get_pitching_potential_ratings(pitching_ratings)
        else:
            pitches = self.get_pitching_ratings(pitching_ratings)
        pitches.sort()

        pitch1rating = pitches[0]
        pitch2rating = pitches[1] if len(pitches) > 1 else 0
        pitch3rating = pitches[2] if len(pitches) > 2 else 0
        pitch4rating = pitches[3] if len(pitches) > 3 else 0

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
                    (pitch1rating * 40)
                    + (pitch2rating * 40)
                    + (pitching_ratings.velocity - 90.0) * 0
                )
            ) * RP_INDIVIDUAL_PITCHING_ADJUSTMENT

    def calculate_starter_pitcher_rating(self, pitching_ratings, position, potential):
        if pitching_ratings.numpitches < 3:
            return 0, 0, 0

        baserating = self.calculate_base_starting_pitching_rating(
            pitching_ratings, position, potential
        )
        indiv_rating = self.calculate_individual_pitch_ratings(
            pitching_ratings, position, potential
        )

        rating = (
            (baserating * SP_BASE_ADJUST)
            + (indiv_rating * SP_PITCH_ADJUST)
            + SP_NORMALIZATION
        )

        return int(round(rating)), int(round(baserating)), int(round(indiv_rating))

    def calculate_relief_pitcher_rating(self, pitching_ratings, position, potential):
        baserating = self.calculate_base_relief_pitching_rating(
            pitching_ratings, position, potential
        )
        indiv_rating = self.calculate_individual_pitch_ratings(
            pitching_ratings, position, potential
        )

        rating = (
            (baserating * RP_BASE_ADJUST)
            + (indiv_rating * RP_PITCH_ADJUST)
            + RP_NORMALIZATION
        )

        return int(round(rating)), int(round(baserating)), int(round(indiv_rating))
