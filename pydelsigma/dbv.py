import numpy as np
from pydelsigma import undbv

def dbv(x):
	""" dbv(x) = 20*log10(abs(x)); the dB equivalent of the voltage x"""
	if not len(x):
		return
	y = -np.inf*np.ones(x.shape)
	nonzero = (x != 0)
	y[nonzero] = 20.*np.log10(np.abs(x[nonzero]))
	return y

def test_dbv():
	import undbv
	t = np.array([3.0])
	r1 = undbv.undbv(dbv(t))
	assert np.allclose(t, r1, atol=1e-8, rtol=1e-5)

if __name__ == '__main__':
	test_dbv()
