import numpy as np

class Trans_MO:

    def __init__(self):

        self.dx = 0
        self.dy = 0
        self.dz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.xbog = 0
        self.ybog = 0
        self.zbog = 0
        self.fac_conver = 0
        self.xsir = 0
        self.ysir = 0
        self.zsir = 0
        self.lat = 0
        self.lon = 0

    def mtz_MO_sir(self):
        
        mtz_0 = np.array([[self.x0],[self.y0],[self.z0]])
        mtz_delta = np.array([[self.dx],[self.dy],[self.dz]])
        escalar = np.array([[1 + self.fac_conver]])
        mtz_rot = np.array([[1,self.rz,-self.ry],[-self.rz,1,self.rx],[self.ry,-self.rx,1]])
        mtz_in = np.array([[self.xbog - self.x0],[self.ybog - self.y0],[self.zbog - self.z0]])
        res1 = escalar * mtz_rot
        res2 = res1 @ mtz_in
        mtz_fin = mtz_0 + mtz_delta + res2
        self.xsir = mtz_fin[0,0]
        self.ysir = mtz_fin[1,0]
        self.zsir = mtz_fin[2,0]

    def ts_MO(self):

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

            self.dx = 311.118
            self.dy = 289.167
            self.dz = -310.641
            self.fac_conver = -5.771882e-6
            self.rx = -8.358815e-5
            self.ry = -3.057474e-5
            self.rz = 7.573043e-6
            self.x0 = 1555622.801
            self.y0 = -6105353.313
            self.z0 = 991255.656
            
        #region 4
        elif self.lat >= 5.0 and self.lat <= 9.4 and self.lon >= -74.4 and self.lon <= -72.0:

            self.dx = 306.666
            self.dy = 315.063
            self.dz = -318.837
            self.fac_conver = -1.389912e-5
            self.rx = -7.992173e-5
            self.ry = -8.090698e-6
            self.rz = 1.051699e-4
            self.x0 = 1845222.398
            self.y0 = -6058604.495
            self.z0 = 769132.398
            
        #region 5
        elif self.lat >= 5.0 and self.lat <= 8.0 and self.lon >= -78.0 and self.lon <= -74.4:

            self.dx = 307.871
            self.dy = 305.803
            self.dz = -311.992
            self.fac_conver = 2.181655e-6
            self.rx = -4.216368e-5
            self.ry = -2.030416e-5
            self.rz = -6.209624e-5
            self.x0 = 1594396.206
            self.y0 = -6143812.398
            self.z0 = 648855.829
            
        #region 6
        elif self.lat >= 3.0 and self.lat <= 5.0 and self.lon >= -78.0 and self.lon <= -74.4:

            self.dx = 302.934
            self.dy = 307.805
            self.dz = -312.121
            self.fac_conver = 3.746562e-6
            self.rx = 3.329153e-5
            self.ry = -4.001009e-5
            self.rz = -4.507205e-5
            self.x0 = 1558280.49
            self.y0 = -6167355.092
            self.z0 = 491954.2193
            
        #region 7
        elif self.lat >= -1.0 and self.lat <= 3.0 and self.lon >= -79.0 and self.lon <= -74.0:

            self.dx = 295.282
            self.dy = 321.293
            self.dz = -311.001
            self.fac_conver = 6.325744e-6
            self.rx = -4.698084e-5
            self.ry = 5.003127e-6
            self.rz = -9.578653e-5
            self.x0 = 1564000.62
            self.y0 = -6180004.879
            self.z0 = 243257.9554
            
        #region 8
        elif ( self.lat >= -4.5 and self.lat <= 3.0 and self.lon >= -74.0 and self.lon <= 66.5) or (self.lat >= 3.0 and self.lat <= 5.0 and self.lon >= -74.0 and self.lon <= -66.5) or (self.lat >= 5.0 and self.lat <= 7.3 and self.lon >= -72.0 and self.lon <= -66.5):

            self.dx = 302.259
            self.dy = 317.979
            self.dz = -319.080
            self.fac_conver = -2.199976e-6
            self.rx = 1.361566e-5
            self.ry = -2.174456e-6
            self.rz = -1.362418e-5
            self.x0 = 1738580.767
            self.y0 = -6120500.388
            self.z0 = 491473.3064

