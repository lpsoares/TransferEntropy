% Input Rets (log-returns for all time series)
[M N]=size(Rets);
% Set step for the calculation of the probability distributions.
passo=0.05;
% Calculates minimum and maximum values, according to step
Peq=min(min(Rets));
Gran=max(max(Rets));
minihist=passo*floor((1/passo)*Peq);
maxihist=passo*ceil((1/passo)*Gran);
xhist=minihist:passo:maxihist;
% Starts the sequence of calculations
for i=1:N;
	i
	for j=1:N;
		clear termo;
		clear ProbABC
		clear ProbAB
		clear ProbBC
		clear ProbB
		clear SortedABC
		clear SortedAB
		clear SortedBC
		clear SortedB
		% Collects time series for i, j, and i-1.
		A(1:M-1,1)=Rets(2:M,i);
		B(1:M-1,1)=Rets(1:M-1,i);
		C(1:M-1,1)=Rets(1:M-1,j);
		% Writes the distributions according to the symbols.
		for L=1:M-1
			classific(L,1)=ceil((A(L,1)-minihist)/passo);
			classific(L,2)=ceil((B(L,1)-minihist)/passo);
			classific(L,3)=ceil((C(L,1)-minihist)/passo);
		end
		% Sorts rows.
		SortedABC=sortrows(classific,[1 2 3]);
		TempoAB(:,1:2)=classific(:,1:2);
		SortedAB=sortrows(TempoAB,[1 2]);
		TempoBC(:,1:2)=classific(:,2:3);
		SortedBC=sortrows(TempoBC,[1 2]);
		TempoB(:,1)=classific(:,2);
		SortedB=sortrows(TempoB);
		% Calculates probability distributions
		clear Au
		clear I
		clear J
		clear Count
		[Au I J]=unique(SortedABC,'rows');
		Count=accumarray(J,1);
		ProbABC(:,1:3)=Au(:,1:3);
		ProbABC(:,4)=Count(:,1);
		clear Au
		clear I
		clear J
		clear Count
		[Au I J]=unique(SortedAB,'rows');
		Count=accumarray(J,1);
		ProbAB(:,1:2)=Au(:,1:2);
		ProbAB(:,3)=Count(:,1);
		clear Au
		clear I
		clear J
		clear Count
		[Au I J]=unique(SortedBC,'rows');
		Count=accumarray(J,1);
		ProbBC(:,1:2)=Au(:,1:2);
		ProbBC(:,3)=Count(:,1);
		clear Au
		clear I
		clear J
		clear Count
		[Au I J]=unique(SortedB,'rows');
		Count=accumarray(J,1);
		ProbB(:,1)=Au(:,1);
		ProbB(:,2)=Count(:,1);
		% Calculates transfer entropy
		[U,V]=size(ProbABC);
		for k=1:U
			caixa(1,1:3)=ProbABC(k,1:3);
			num1=0;
			[oi,oj]=size(ProbAB);
			for ele=1:oi
				if ProbABC(k,1:2)==ProbAB(ele,1:2)
					num1=ele;
				end
			end
			num2=0;
			[oi,oj]=size(ProbBC);
			for ele=1:oi
				if ProbABC(k,2:3)==ProbBC(ele,1:2)
					num2=ele;
				end
			end
			num3=0;
			[oi,oj]=size(ProbB);
			for ele=1:oi
				if ProbABC(k,2)==ProbB(ele,1)
					num3=ele;
				end
			end
			if num1*num2*num3==0
				termo(k,1)=0;
			else
				termo(k,1)=(ProbABC(k,4)/(M-1))*log((ProbABC(k,4)*ProbB(num3,2))/(ProbBC(num2,3)*ProbAB(num1,3)))/log(2);
			end
		end
		TE(i,j)=sum(termo);
	end
end
