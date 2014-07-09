CREATE VIEW 
	extended
AS
	SELECT * FROM frequency
	UNION
	SELECT 'q' as docid, 'washington' as term, 1 as count 
	UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
	UNION 
	SELECT 'q' as docid, 'treasury' as term, 1 as count

SELECT
	*
FROM (
	SELECT 
		a.docid AS adoc, b.docid AS bdoc, SUM(a.count * b.count) AS score
	FROM 
		extended as a,
		extended as b
	WHERE
		a.term = b.term
	GROUP BY a.docid, b.docid ) x
WHERE
	x.adoc < x.bdoc
	AND x.adoc = 'q'
ORDER BY x.score DESC
