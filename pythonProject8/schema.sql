drop table if exists trackks;
create table trackks as
select t.TrackId, t.Name as 'title', count(i.InvoiceId) as 'count' FROM tracks t
join albums a ON t.AlbumId = a.AlbumId
join artists a2 ON a.ArtistId = a2.ArtistId
join invoice_items ii ON t.TrackId = ii.TrackId
join invoices i ON ii.InvoiceId = i.InvoiceId
group by i.InvoiceId;
