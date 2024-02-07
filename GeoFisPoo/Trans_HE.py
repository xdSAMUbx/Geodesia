class Trans_HE:
    def __init__(self):

        self.dx = 0
        self.dy = 0
        self.dz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.xbog = 0
        self.ybog = 0
        self.zbog = 0
        self.fac_conver = 0
        self.xsir = 0
        self.ysir = 0
        self.zsir = 0
        self.lat = 0
        self.lon = 0
        self.h = 0
    
    def mtz_HE_sir(self):
        pass

    def ts_HE(self):
        
        #region 1
        if self.lat >= 10.0 and self.lat <= 13.0 and self.lon >= -73.0 and self.lon <= -71.0:

            self.dx = 300.449
            self.dy = 293.757
            self.dz = -317.306
            self.fac_conver = -2.081615e-5
            self.rx = 6.018581e-5
            self.ry = -1.450002e-5
            self.rz = -1.892455e-4
            self.x0 = 1891881.173
            self.y0 = -5961263.267
            self.z0 = 1248403.057
            
        #region 2
        elif self.lat >= 9.4 and self.lat <= 11.6 and self.lon >= -76.0 and self.lon <= -73.0:

            self.dx = 308.833
            self.dy = 282.519
            self.dz = -314.571
            self.fac_conver = -1.356561e-5
            self.rx = -4.471845e-5
            self.ry = 1.175087e-5
            self.rz = -4.027981e-5
            self.x0 = 1625036.590
            self.y0 = -6054644.061
            self.z0 = 1172969.151
            
        #region 3
        elif self.lat >= 8.0 and self.lat <= 9.4 and self.lon >= -77.6 and self.lon <= -74.4:

            self.dx = 
            self.dy = 
            self.dz = 
            self.fac_conver = -5.771909e-6
            self.rx = -8.358813e-5
            self.ry = -3.057474e-5
            self.rz = 7.573031e-6
            self.x0 = 
            self.y0 = 
            self.z0 = 
            
        #region 4
        elif self.lat >= 5.0 and self.lat <= 9.4 and self.lon >= -74.4 and self.lon <= -72.0:

            self.dx = 
            self.dy = 
            self.dz = 
            self.fac_conver = -1.389914e-5
            self.rx = -7.992171e-5
            self.ry = -8.090696e-6
            self.rz = 1.051699e-4
            self.x0 = 
            self.y0 = 
            self.z0 = 
            
        #region 5
        elif self.lat >= 5.0 and self.lat <= 8.0 and self.lon >= -78.0 and self.lon <= -74.4:

            self.dx = 
            self.dy = 
            self.dz = 
            self.fac_conver = 2.181658e-6
            self.rx = -4.216369e-5
            self.ry = -2.030416e-5
            self.rz = -6.209623e-5
            self.x0 = 
            self.y0 = 
            self.z0 = 
            
        #region 6
        elif self.lat >= 3.0 and self.lat <= 5.0 and self.lon >= -78.0 and self.lon <= -74.4:

            self.dx = 
            self.dy = 
            self.dz = 
            self.fac_conver = 3.746560e-6
            self.rx = 3.329153e-5
            self.ry = -4.001009e-5
            self.rz = -4.507206e-5
            self.x0 = 
            self.y0 = 
            self.z0 = 
            
        #region 7
        elif self.lat >= -1.0 and self.lat <= 3.0 and self.lon >= -79.0 and self.lon <= -74.0:

            self.dx = 
            self.dy = 
            self.dz = 
            self.fac_conver = 6.325747e-6
            self.rx = -4.698084e-5
            self.ry = 5.003123e-6
            self.rz = -9.578655e-5
            self.x0 = 
            self.y0 = 
            self.z0 = 
            
        #region 8
        elif ( self.lat >= -4.5 and self.lat <= 3.0 and self.lon >= -74.0 and self.lon <= 66.5) or (self.lat >= 3.0 and self.lat <= 5.0 and self.lon >= -74.0 and self.lon <= -66.5) or (self.lat >= 5.0 and self.lat <= 7.3 and self.lon >= -72.0 and self.lon <= -66.5):

            self.dx = 
            self.dy = 
            self.dz = 
            self.fac_conver = -2.199943e-6
            self.rx = 1.361573e-5
            self.ry = -2.174431e-6
            self.rz = -1.362410e-5
            self.x0 = 
            self.y0 = 
            self.z0 = 

    def tb_HE(self):
        pass