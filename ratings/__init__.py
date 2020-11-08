from db import Player, PlayerBatting, PlayerFielding, PlayerPitching

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

SHORTSTOP_BASE = 408

CATCHER_FIELD_ADJUST = 0.25
CATCHER_BATTING_ADJUST = 0.75
FIRSTBASE_FIELD_ADJUST = 0.05
FIRSTBASE_BATTING_ADJUST = 0.95
SECONDBASE_FIELD_ADJUST = 0.15
SECONDBASE_BATTING_ADJUST = 0.85
SHORTSTOP_FIELD_ADJUST = 0.40
SHORTSTOP_BATTING_ADJUST = 0.60
THIRDBASE_FIELD_ADJUST = 0.15
THIRDBASE_BATTING_ADJUST = 0.85
LEFTFIELD_FIELD_ADJUST = 0.05
LEFTFIELD_BATTING_ADJUST = 0.95
CENTERFIELD_FIELD_ADJUST = 0.50
CENTERFIELD_BATTING_ADJUST = 0.50
RIGHTFIELD_FIELD_ADJUST = 0.25
RIGHTFIELD_BATTING_ADJUST = 0.75

CATCHER_NORMALIZATION = 17 #2862/3000
SHORTSTOP_NORMALIZATION = -2 #2589/3000
SECONDBASE_NORMALIZATION = 10 #2987/3000
THIRDBASE_NORMALIZATION = 8 #3352/3000
FIRSTBASE_NORMALIZATION = 2 #2840/3000
LEFTFIELD_NORMALIZATION = 7 #2369/3000
CENTERFIELD_NORMALIZATION = -10 #3514/3000
RIGHTFIELD_NORMALIZATION = 5 #3266/3000
DH_NORMALIZATION = 0 #2793/3000


groundball_flyball_adjustment = {
    "EX FB" :-4,
    "FB" : -2,
    "NEU" : 0,
    "GB" : 0,
    "EX GB": 0,
}

BASE_PITCHING_ADJUSTMENT = 0.1182
INDIVIDUAL_PITCHING_ADJUSTMENT = 0.2083

SP_BASE_ADJUST = 0.85
SP_PITCH_ADJUST = 0.15
SP_NORMALIZATION = 12

class PlayerRatings():

    def calc_catcher_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.catcherability*34.5 +
            fielding_ratings.catcherarm*24.5) *
            CATCHER_ADJUSTMENT
        )

        return rating

    def calc_shortstop_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.infieldrange*50.5 +
            fielding_ratings.infieldarm*2 +
            fielding_ratings.turndoubleplay*8 +
            fielding_ratings.infielderror*7.5) *
            SHORTSTOP_ADJUSTMENT
        )

        return rating

    def calc_secondbase_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.infieldrange*40 +
            fielding_ratings.infieldarm*1.5 +
            fielding_ratings.turndoubleplay*9 +
            fielding_ratings.infielderror*8.25) *
            SECONDBASE_ADJUSTMENT
        )

        return rating
            
    def calc_thirdbase_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.infieldrange*13 +
            fielding_ratings.infieldarm*22 +
            fielding_ratings.turndoubleplay*3.25 +
            fielding_ratings.infielderror*7.5) *
            THIRDBASE_ADJUSTMENT
        )

        return rating

    def calc_firstbase_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.infieldrange*2 +
            fielding_ratings.infieldarm*0.75 +
            fielding_ratings.turndoubleplay*0.75 +
            fielding_ratings.infielderror*2) *
            FIRSTBASE_ADJUSTMENT
        )

        return rating

    def calc_leftfield_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.outfieldrange*33.5 +
            fielding_ratings.outfieldarm*3 +
            fielding_ratings.outfielderror*2) *
            LEFTFIELD_ADJUSTMENT
        )

        return rating

    def calc_centerfield_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            (fielding_ratings.outfieldrange*35 +
            fielding_ratings.outfieldarm*1.75 +
            fielding_ratings.outfielderror*3.5) *
            CENTERFIELD_ADJUSTMENT
        )

        return rating

    def calc_rightfield_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        rating = (
            ((fielding_ratings.outfieldrange*36.5) +
            (fielding_ratings.outfieldarm*4) +
            (fielding_ratings.outfielderror*1)) *
            RIGHTFIELD_ADJUSTMENT
        )

        return rating

    def calc_dh_defense_rating(self, fielding_ratings: PlayerFielding) -> int:
        return 0.0

    fielding_calc = {
        "1B": calc_firstbase_defense_rating,
        "2B": calc_secondbase_defense_rating,
        "SS": calc_shortstop_defense_rating,
        "3B": calc_thirdbase_defense_rating,
        "C" : calc_catcher_defense_rating,
        "LF": calc_leftfield_defense_rating,
        "CF": calc_centerfield_defense_rating,
        "RF": calc_rightfield_defense_rating,
        "DH": calc_dh_defense_rating
    }
    
    
    def calculate_defense_rating(self, fielding_ratings, position):
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
        elif position == "SP" or position == "RP" or position == "CL":
            rating = 0.0
        else:
            print (f'Invalid position {position}')
            rating = 0.0

        return int(round(rating))

    def squared_diff(self, rating):
        decrement = -1 if rating < 6 else 1
        result = ((rating-6)*(rating-6)*decrement)+25
        print(f'rating {rating}  result {result}')
        return result
    
    def calculate_batting_rating(self, batting_ratings, position):
        if batting_ratings.battedballtype == 'Flyball':
            type_adjustment = 3
        elif batting_ratings.battedballtype == 'Groundball':
            type_adjustment = -3
        else:
            type_adjustment = 0

        if position == "C":
            rating = (
                ((batting_ratings.contactrating*19) +
                (batting_ratings.gaprating*5) +
                (batting_ratings.powerrating*19) +
                (batting_ratings.eyerating*19) +
                (batting_ratings.krating*19) +
                (batting_ratings.speedrating*15) +
                (type_adjustment*4)) *
                CATCHER_BATTING_ADJUSTMENT
            )
        else:
            rating = (
                ((batting_ratings.contactrating*19) +
                (batting_ratings.gaprating*5) +
                (batting_ratings.powerrating*19) +
                (batting_ratings.eyerating*19) +
                (batting_ratings.krating*19) +
                (type_adjustment*4)) *
                BATTING_ADJUSTMENT
            )

        return int(round(rating))

    def calculate_overall_batter_rating(self, fielding_ratings, batting_ratings, position):
        brating = self.calculate_batting_rating(batting_ratings, position)
        frating = self.calculate_defense_rating(fielding_ratings, position)
        if position == "1B":
            rating = (brating*FIRSTBASE_BATTING_ADJUST + frating*FIRSTBASE_FIELD_ADJUST)+FIRSTBASE_NORMALIZATION
        elif position == "2B":
            rating = (brating*SECONDBASE_BATTING_ADJUST + frating*SECONDBASE_FIELD_ADJUST)+SECONDBASE_NORMALIZATION
        elif position == "SS":
            rating = (brating*SHORTSTOP_BATTING_ADJUST + frating*SHORTSTOP_FIELD_ADJUST)+SHORTSTOP_NORMALIZATION
        elif position == "3B":
            rating = (brating*THIRDBASE_BATTING_ADJUST + frating*THIRDBASE_FIELD_ADJUST)+THIRDBASE_NORMALIZATION
        elif position == "LF":
            rating = (brating*LEFTFIELD_BATTING_ADJUST + frating*LEFTFIELD_FIELD_ADJUST)+LEFTFIELD_NORMALIZATION
        elif position == "CF":
            rating = (brating*CENTERFIELD_BATTING_ADJUST + frating*CENTERFIELD_FIELD_ADJUST)+CENTERFIELD_NORMALIZATION
        elif position == "RF":
            rating = (brating*RIGHTFIELD_BATTING_ADJUST + frating*RIGHTFIELD_FIELD_ADJUST)+RIGHTFIELD_NORMALIZATION
        elif position == "C":
            rating = (brating*CATCHER_BATTING_ADJUST + frating*CATCHER_FIELD_ADJUST)+CATCHER_NORMALIZATION
        elif position == "DH":
            rating = brating+DH_NORMALIZATION
        elif position == "SP" or position == "RP" or position == "CL":
            rating = 0.0
        else:
            print (f'Invalid position {position}')
            rating = 0.0

        return int(round(rating))



    def calculate_base_pitching_rating(self, pitching_ratings, position):

        gb_fb_adjustment = groundball_flyball_adjustment[pitching_ratings.groundballflyball]

        rating = (
            ((gb_fb_adjustment*15) +
            (pitching_ratings.stuffrating*37) +
            (pitching_ratings.movementrating*35) +
            (pitching_ratings.controlrating*34) +
            (pitching_ratings.stamina*10)) *
            BASE_PITCHING_ADJUSTMENT
        )

        return rating

    def get_pitching_ratings(self, pitching_ratings):
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




    def calculate_individual_pitch_ratings(self, pitching_ratings, position):

        pitches = self.get_pitching_ratings(pitching_ratings)
        pitches.sort()

        pitch1rating = pitches[0]
        pitch2rating = pitches[1] if len(pitches) > 1 else 0
        pitch3rating = pitches[2] if len(pitches) > 2 else 0
        pitch4rating = pitches[3] if len(pitches) > 3 else 0

        rating = (
            ((pitch1rating*20) +
            (pitch2rating*20) +
            (pitch3rating*10) +
            (pitch4rating*10) + 
            (pitching_ratings.velocity-90.0)*20) *
            INDIVIDUAL_PITCHING_ADJUSTMENT 
        )

        return rating

        


    def calculate_starter_pitcher_rating(self, pitching_ratings, position):
        baserating = self.calculate_base_pitching_rating(pitching_ratings, position)
        indiv_rating = self.calculate_individual_pitch_ratings(pitching_ratings, position)

        rating = (baserating*SP_BASE_ADJUST) + (indiv_rating*SP_PITCH_ADJUST) + SP_NORMALIZATION
        
        return int(round(rating))
