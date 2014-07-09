SELECT 
	count(*) 
FROM (
	SELECT 
		*
	FROM 
		frequency AS f1,
		frequency AS f2
	WHERE	
		f1.docid = f2.docid 
		AND f1.term = 'transactions'
		AND f2.term = 'world'
) x;
