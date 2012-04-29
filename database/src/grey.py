import numpy

def diff_min_max(x,y):
	t=abs(x-y)
	return t.max(),t.min()

def grey(x1,y1,rho=0.5):
	x=x1/(x1.mean())
	y=numpy.copy(y1)
	y_m=y1.mean(axis=1)
	y_len,xxx=y.shape
	for i in range(0,y_len):
		y[i]=y[i]/(y_m[i])
	
	mnarray=[]
	mxarray=[]
	for i in range(0, y_len):
		mx,mn=diff_min_max(x,y[i])
		mnarray.append(mn)
		mxarray.append(mx)
	minmin=min(mnarray)
	maxmax=max(mxarray)
	
	result=[]
	for i in range(0, y_len):
		diff=abs(x-y[i])
		res=(minmin+rho*maxmax)/(diff+rho*maxmax)
		result.append(res.mean())
	ret_val=numpy.array(result)
	return ret_val

if __name__=="__main__":
    print grey(numpy.array([1.0,2,3])
              ,numpy.array([[2.0,5,4],[4.0,10,6]]))

