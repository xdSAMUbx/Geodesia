
class Trans_LA:

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

    def mtz_LA_sir(self):

        self.xsir = self.dx + self.xbog + self.rz*self.ybog - self.ry*self.zbog + self.xbog*self.fac_conver
        self.ysir = self.dy + self.ybog - self.rz*self.xbog + self.rx*self.zbog + self.ybog*self.fac_conver
        self.zsir = self.dz + self.zbog + self.ry*self.xbog - self.rx*self.ybog + self.zbog*self.fac_conver

    def ts_LA(self):

        #region 1
        if self.lat >= 10.0 and self.lat <= 13.0 and self.lon >= -73.0 and self.lon <= -71.0:

            self.dx = -806.413
            self.dy = -263.500
            self.dz = -622.671
            self.fac_conver = -2.081616e-5
            self.rx = 6.018583e-5
            self.ry = -1.450001e-5
            self.rz = -1.892455e-4
            
        #region 2
        elif self.lat >= 9.4 and self.lat <= 11.6 and self.lon >= -76.0 and self.lon <= -73.0:

            self.dx = 100.783
            self.dy = 187.382
            self.dz = -47.000
            self.fac_conver = -1.356561e-5
            self.rx = -4.471839e-5
            self.ry = 1.175093e-5
            self.rz = -4.027967e-5
            
        #region 3
        elif self.lat >= 8.0 and self.lat <= 9.4 and self.lon >= -77.6 and self.lon <= -74.4:

            self.dx = 336.026
            self.dy = 348.565
            self.dz = 252.978
            self.fac_conver = -5.771909e-6
            self.rx = -8.358813e-5
            self.ry = -3.057474e-5
            self.rz = 7.573031e-6
            
        #region 4
        elif self.lat >= 5.0 and self.lat <= 9.4 and self.lon >= -74.4 and self.lon <= -72.0:

            self.dx = 963.273
            self.dy = 486.386
            self.dz = 190.997
            self.fac_conver = -1.389914e-5
            self.rx = -7.992171e-5
            self.ry = -8.090696e-6
            self.rz = 1.051699e-4
            
        #region 5
        elif self.lat >= 5.0 and self.lat <= 8.0 and self.lon >= -78.0 and self.lon <= -74.4:

            self.dx = -90.290
            self.dy = 247.559
            self.dz = -21.989
            self.fac_conver = 2.181658e-6
            self.rx = -4.216369e-5
            self.ry = -2.030416e-5
            self.rz = -6.209623e-5
            
        #region 6
        elif self.lat >= 3.0 and self.lat <= 5.0 and self.lon >= -78.0 and self.lon <= -74.4:

            self.dx = -0.562
            self.dy = 244.299
            self.dz = -456.938
            self.fac_conver = 3.746560e-6
            self.rx = 3.329153e-5
            self.ry = -4.001009e-5
            self.rz = -4.507206e-5
            
        #region 7
        elif self.lat >= -1.0 and self.lat <= 3.0 and self.lon >= -79.0 and self.lon <= -74.0:

            self.dx = -305.356
            self.dy = 222.004
            self.dz = -30.023
            self.fac_conver = 6.325747e-6
            self.rx = -4.698084e-5
            self.ry = 5.003123e-6
            self.rz = -9.578655e-5
            
        #region 8
        elif ( self.lat >= -4.5 and self.lat <= 3.0 and self.lon >= -74.0 and self.lon <= 66.5) or (self.lat >= 3.0 and self.lat <= 5.0 and self.lon >= -74.0 and self.lon <= -66.5) or (self.lat >= 5.0 and self.lat <= 7.3 and self.lon >= -72.0 and self.lon <= -66.5):

            self.dx = 221.899
            self.dy = 274.136
            self.dz = -397.554
            self.fac_conver = -2.199943e-6
            self.rx = 1.361573e-5
            self.ry = -2.174431e-6
            self.rz = -1.362410e-5

    def tb_LA (self):
        pass
    