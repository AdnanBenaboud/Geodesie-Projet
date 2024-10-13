
import math as m



class GeoPosition:
    def __init__(self,phi,lam,h):
        self.phi = phi
        self.lam = lam
        self.h = h


class CartPosition:
    def __init__(self,X,Y,Z):
        self.X = X
        self.Y = Y
        self.Z = Z

class WGS84:

    def __init__(self):
        self.a = 6378137
        self.b = 6356752.3142
        self.e2 = (m.pow(self.a,2)-m.pow(self.b,2))/m.pow(self.a,2)

    def geoToCart(self, position):
        
        N = self.a / m.sqrt(1-(self.e2*m.pow(m.sin(position.phi),2)))
        X = (N+position.h)*m.cos(position.lam)*m.cos(position.phi)
        Y = (N+position.h)*m.sin(position.lam)*m.cos(position.phi)
        Z=(N*(1-m.pow(self.e2,2))+position.h)*m.sin(position.phi)

        return X,Y,Z



    def CartToGeo(self, position):
        lam = m.atan2(position.Y,position.X)

        phi= m.atan2(position.Z,m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))

        N = self.a / m.sqrt(1-(self.e2*m.pow(m.sin(phi),2)))

        h = ((m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))/m.cos(phi))-N

        phi_pre=phi
        
        while(True):

            phi = m.atan2(position.Z,(m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))*(1-self.e2*(N/(N+h))))
            N = self.a / m.sqrt(1-(self.e2*m.pow(m.sin(phi),2)))
            h = ((m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))/m.cos(phi))-N

            if(m.fabs((phi-phi_pre)/phi)) < 0.0001:
                break

            phi_pre = phi

        return phi,lam,h

class Clarke_1880:

    def __init__(self):
        self.a = 6378249
        self.b = 6356515
        self.e2 = (m.pow(self.a,2)-m.pow(self.b,2))/m.pow(self.a,2)
    



    def geoToCart(self, position):
        
        N = self.a / m.sqrt(1-(self.e2*m.pow(m.sin(position.phi),2)))
        X = (N+position.h)*m.cos(position.lam)*m.cos(position.phi)
        Y = (N+position.h)*m.sin(position.lam)*m.cos(position.phi)
        Z=(N*(1-m.pow(self.e2,2))+position.h)*m.sin(position.phi)

        return X,Y,Z



    def CartToGeo(self, position):
        lam = m.atan2(position.Y,position.X)

        phi= m.atan2(position.Z,m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))

        N = self.a / m.sqrt(1-(self.e2*m.pow(m.sin(phi),2)))

        h = ((m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))/m.cos(phi))-N

        phi_pre=phi
        
        while(True):

            phi = m.atan2(position.Z,(m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))*(1-self.e2*(N/(N+h))))
            N = self.a / m.sqrt(1-(self.e2*m.pow(m.sin(phi),2)))
            h = ((m.sqrt(m.pow(position.X,2)+m.pow(position.Y,2)))/m.cos(phi))-N

            if(m.fabs((phi-phi_pre)/phi)) < 0.0001:
                break

            phi_pre = phi

        return phi,lam,h



    
        
