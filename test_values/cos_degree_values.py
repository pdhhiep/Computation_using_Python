#!/usr/bin/env python
#
def cos_degree_values ( n_data ):

#*****************************************************************************80
#
## COS_DEGREE_VALUES: the cosine function with argument in degrees.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cos[x Degree]
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 22

  fx_vec = np.array ( ( \
     0.99619469809174553230, \
     1.0000000000000000000, \
     0.99984769515639123916, \
     0.99939082701909573001, \
     0.99862953475457387378, \
     0.99756405025982424761, \
     0.99619469809174553230, \
     0.98480775301220805937, \
     0.96592582628906828675, \
     0.86602540378443864676, \
     0.70710678118654752440, \
     0.50000000000000000000, \
     0.25881904510252076235, \
     0.087155742747658173558, \
     0.069756473744125300776, \
     0.052335956242943832722, \
     0.034899496702500971646, \
     0.017452406437283512819, \
     0.000000000000000000000, \
    -0.017452406437283512819, \
    -0.25881904510252076235, \
    -1.0000000000000000000 ))

  x_vec = np.array ( ( \
     -5.0, \
      0.0, \
      1.0, \
      2.0, \
      3.0, \
      4.0, \
      5.0, \
     10.0, \
     15.0, \
     30.0, \
     45.0, \
     60.0, \
     75.0, \
     85.0, \
     86.0, \
     87.0, \
     88.0, \
     89.0, \
     90.0, \
     91.0, \
    105.0, \
    180.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def cos_degree_values_test ( ):

#*****************************************************************************80
#
## COS_DEGREE_VALUES_TEST demonstrates the use of COS_DEGREE_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'COS_DEGREE_VALUES_TEST:'
  print '  COS_DEGREE_VALUES stores values of the cosine function.'
  print ''
  print '      X         COS(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = cos_degree_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'COS_DEGREE_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cos_degree_values_test ( )
  timestamp ( )

