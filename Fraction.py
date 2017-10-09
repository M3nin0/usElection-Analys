class Fraction():
    
    # Retorna estados com votos maiores que 300 mil
    def fract_votes_filter(self, x):
        return x['votes'].sum() > 300000