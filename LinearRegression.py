# %%
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
import itertools
# %%
def get_data(
    nsamples=500,
    ndim=2,
    intrinsic_noise=0.1,
    correlation=0.0,
    std=None,
    coefficients=None,
):
    if std is None:
        std = np.ones(ndim)
    s1, s2 = std
    cov = [[s1**2, s1 * s2 * correlation], [s1 * s2 * correlation, s2**2]]
    if coefficients is None:
        coefficients = np.ones(ndim).reshape(ndim, 1)
    X_true = np.random.multivariate_normal(np.zeros(ndim), cov, size=nsamples)
    y = X_true @ coefficients + np.random.normal(
        size=(nsamples, 1), scale=intrinsic_noise
    )
    return X_true, y


X_true, y = get_data()


class Regressor:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.beta = np.linalg.pinv(X.T @ X) @ X.T @ y
        self.TSS = np.sum((y - np.mean(y)) ** 2)
        self.RSS = np.sum((y - X @ self.beta) ** 2)
        self.R2 = 1 - self.RSS / self.TSS

    def predict(self, X):
        return X @ self.beta


X = X_true[:, :1]
solution = Regressor(X, y)
print("Coeff = ", solution.beta)
print("R2 = ", solution.R2)
xplot = np.linspace(-2, 2, 100).reshape(100, 1)
yplot = solution.predict(xplot)
plt.scatter(X[:, 0], y)
plt.plot(xplot, yplot, "r")
plt.title(
    r"Linear regression RSS {:.2f}, TSS {:.2f}, R2 {:.2f}".format(
        solution.RSS, solution.TSS, solution.R2
    )
)
plt.show()
# plt.scatter(X_true[:, 0], X_true[:, 1])
# plt.title('True data')
# plt.show()


# %%
corr_list = np.linspace(-1, 1, 100)
R2_list = []
R2_list2 = []
R2_list3 = []
betas = []
betas2 = []
for corr in corr_list:
    X_true, y = get_data(
        correlation=corr,
        intrinsic_noise=0.0,
        std=[2, 1],
        ndim=2,
        nsamples=500,
        coefficients=np.array([[1.], [1]]),
    )
    X = X_true[:, :1]
    solution = Regressor(X, y)
    R2_list.append(solution.R2)
    betas.append(solution.beta[0, 0])
    X = X_true[:, 1:]
    solution = Regressor(X, y)
    R2_list2.append(solution.R2)
    betas2.append(solution.beta[0, 0])
    X = X_true
    solution = Regressor(X, y)
    R2_list3.append(solution.R2)
ax = plt.subplot(111)
ax.plot(corr_list, R2_list, c='blue', label="first feature")
ax.plot(corr_list, R2_list2, c='green', label="second feature")
ax.plot(corr_list, R2_list3, lw=3, c="red", label="both features")
ax.set_xlabel("Correlation")
ax.set_ylabel("R2")
ax.set_ylim(0, 1 + 1e-3)
ax1 = ax.twinx()
ax1.plot(corr_list, betas, "b", ls="--")
ax1.plot(corr_list, betas2, "g", ls="--")
ax1.spines["right"].set_color("red")
ax1.set_ylabel("Beta")
ax.legend()
plt.show()
# %%
class Regressor:
    def __init__(self, X, y, fit_intercept=True, ridge=0):
        self.fit_intercept = fit_intercept
        self.intercept = np.zeros(1)
        if fit_intercept:
            self.xmean = np.mean(X, axis=0)
            self.ymean = np.mean(y)
            X = X - self.xmean
            y = y - self.ymean
        self.beta = np.linalg.inv(X.T @ X + ridge * np.eye(X.shape[1])) @ X.T @ y
        if fit_intercept:
            self.intercept = self.ymean - self.xmean @ self.beta
        self.TSS = np.sum((y - np.mean(y)) ** 2)
        self.RSS = np.sum((y - X @ self.beta) ** 2)
        self.R2 = 1 - self.RSS / self.TSS

    def predict(self, X):
        return X @ self.beta + self.intercept
    def __repr__(self) -> str:
        return f"Regressor(beta={self.beta.flatten()}, intercept={self.intercept[0]}), R2={self.R2}"


# %%
np.random.seed(1)
X_true, y = get_data(nsamples=500, ndim=2, intrinsic_noise=1e-3, 
        correlation=0, std=[1, 2], coefficients=np.array([[2], [1]]))

X = X_true[:, 1:]
solution = Regressor(X, y, fit_intercept=False, ridge=0.1)
print(solution)
# generate a ndim grid of points to plot the regression line
xplot = np.linspace(-2, 2, 100)
xplot = np.array(list(itertools.product(xplot, repeat=X.shape[1])))
yplot = solution.predict(xplot).reshape(100, -1).mean(axis=1)
xplot = xplot[:, 0].reshape(100, -1).mean(axis=1)
plt.scatter(X[:, 0], y)
plt.plot(xplot, yplot, "r")
plt.title(
    r"Linear regression RSS {:.2f}, TSS {:.2f}, R2 {:.2f}".format(
        solution.RSS, solution.TSS, solution.R2
    )
)
plt.show()
# %%
result = LinearRegression(fit_intercept=True).fit(X, y)
print(result.__dict__)
# %%
np.linalg.eigvals(X.T @ X)
# %%
X = X_true[:, :1]
result = linregress(X.flatten(), y.flatten())
print(result)


# %%
mat = np.eye(3)[:, :2] * np.arange(1, 3).reshape(1, 2)
print(mat)
inv = np.linalg.pinv(mat)
print("inv", inv, sep="\n")
print("inv @ mat", inv @ mat, sep="\n")
print("mat @ inv", mat @ inv, sep="\n")

# %%
