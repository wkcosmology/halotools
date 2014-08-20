#!/usr/bin/env python

from __future__ import division, print_function

from ..observables import two_point_correlation_function
import numpy as np

def test_TPCF_auto():

    sample1 = np.random.random((100,3))
    sample2 = np.random.random((100,3))
    randoms = np.random.random((100,3))
    period = np.array([1,1,1])
    rbins = np.linspace(0,0.5,5)
    
    #with randoms
    result = two_point_correlation_function(sample1, rbins, sample2 = None, 
                                            randoms=randoms, period = None, 
                                            max_sample_size=int(1e4), estimator='Natural')
    assert result.ndim == 1, "More than one correlation function returned erroneously."


def test_TPCF_estimator():

    sample1 = np.random.random((100,3))
    sample2 = np.random.random((100,3))
    randoms = np.random.random((100,3))
    period = np.array([1,1,1])
    rbins = np.linspace(0,0.5,5)
    
    result_1 = two_point_correlation_function(sample1, rbins, sample2 = sample2, 
                                            randoms=randoms, period = None, 
                                            max_sample_size=int(1e4), estimator='Natural')
    result_2 = two_point_correlation_function(sample1, rbins, sample2 = sample2, 
                                            randoms=randoms, period = None, 
                                            max_sample_size=int(1e4), estimator='Davis-Peebles')
    result_3 = two_point_correlation_function(sample1, rbins, sample2 = sample2, 
                                            randoms=randoms, period = None, 
                                            max_sample_size=int(1e4), estimator='Hewett')
    result_4 = two_point_correlation_function(sample1, rbins, sample2 = sample2, 
                                            randoms=randoms, period = None, 
                                            max_sample_size=int(1e4), estimator='Hamilton')
    result_5 = two_point_correlation_function(sample1, rbins, sample2 = sample2, 
                                            randoms=randoms, period = None, 
                                            max_sample_size=int(1e4), estimator='Landy-Szalay')
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)
    assert True==False, "More than one correlation function returned erroneously."