

class DivModel:

    def __init__(self):
        set_default_values()
        init_est_divStream_time()
        pass


    def set_default_values(self):
        self.M = 0
        self.V = 0
        self.K = 100
        self.alpha = 50.0 / K
        self.beta = 0.1
        self.niters = 2000
        self.liter = 0
        self.savestep = 200
        self.twords = 0
        self.withrawstrs = 0

        self.p = None
        self.z = None
        self.nw = None
        self.nd = None
        self.nwsum = None
        self.ndsum = None
        self.theta = None
        self.phi = None

        self.newM = 0
        self.newV = 0
        self.newz = None
        self.newnw = None
        self.newnd = None
        self.newnwsum = None
        self.newndsum = None
        self.newtheta = None
        self.newphi = None


    def init_est_divStream_time(self):
        self.p = [0.0]*self.K
        # 从数据集得到!!!
        self.M = 0
        self.V = 0
        # std::string minTimFilStr
        # ptrndata = new dataset
        # M = ptrndata->M
        # V = ptrndata->V
        self.alpha_tim = [0.0]*self.K
        self.beta_tim = [0.0]*self.V
        self.theta_tim = [0.0]*self.K
        self.phi_tim = [[0.0]*self.K]*self.V
        self.zd_tim = [0]*self.M
        self.mz_tim = [0]*self.K
        self.nz_tim = [0]*self.K
        for k in range(self.K):
            self.alpha_tim[k] = self.alpha
        for v in range(self.V):
            self.beta_tim[v] = self.beta
        for k in range(self.K):
            self.theta_tim[k] = 1.0 / (self.K * 1.0)
            self.mz_tim[k] = 0
            self.nz_tim[k] = 0
            for v in range(self.V):
                self.phi_tim[k][v] = 1.0 / (self.V * 1.0)
        self.nw = [[0]*self.V]*self.K
        for v in range(self.V):
            for k in range(self.K):
                self.nw[w][k] = 0
                self.nwsum = [0]*self.K
        for k in range(self.K):
            self.nwsum[k] = 0
        theta = [[0.0]*self.M]*self.K
        phi = [[0.0]*self.K]*self.V


    def estimate_divStream_time(self):
        pass