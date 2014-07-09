SELECT
	*
FROM (
	SELECT 
		a.docid AS adoc, b.docid AS bdoc, SUM(a.count * b.count)
	FROM
		frequency as a,
		frequency as b
	WHERE
		a.term = b.term
	GROUP BY a.docid, b.docid ) x
WHERE
	x.adoc < x.bdoc
	AND x.adoc = '10080_txt_crude' 
	AND x.bdoc = '17035_txt_earn'
