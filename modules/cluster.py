from modules.similarity import pearson_sim
from PIL import Image, ImageDraw


class bicluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance


def pearson(data1, data2):
    pearson_val = pearson_sim(data1, data2)
    return 1 - pearson_val


def hcluster(rows, distance=pearson):
    distances = {}
    currentclustid = -1

    clust = [bicluster(rows[i], id=i) for i in range(len(rows))]

    while len(clust) > 1:
        lowestpair = (0, 1)
        closest = distance(clust[0].vec, clust[1].vec)

        for i in range(len(clust)):
            for j in range(i + 1, len(clust)):
                if (clust[i].id, clust[j].id) not in distances:
                    distances[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)
                d = distances[((clust[i].id, clust[j].id))]
                if d < closest:
                    closest = d
                    lowestpair = (i, j)
        mergevec = [(clust[lowestpair[0]].vec[i] + clust[lowestpair[1]].vec[i]) / 2.0 for i in range(len(clust[0].vec))]

        new_cluster = bicluster(mergevec, left=clust[lowestpair[0]], right=clust[lowestpair[1]], distance=closest,
                                id=currentclustid)
        currentclustid = -1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(new_cluster)
    return clust[0]


def getheight(clust):
    if clust.left == None and clust.right == None:
        return 1

    return getheight(clust.left) + getheight(clust.right)


def getdepth(clust):
    if clust.left == None and clust.right == None:
        return 0
    return max(getdepth(clust.left), getdepth(clust.right)) + clust.distance


def drawdendrogram(clust, jpeg='cluster.jpg'):
    h = getheight(clust) * 20
    w = 1200
    depth = getdepth(clust)
    scaling = float(w - 150) / depth
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.line((0, h/2, 10, h/2), fill=(255, 0, 0))
    drawnode(draw, clust, 10, (h/2), scaling)
    img.save(jpeg, 'JPEG')


def drawnode(draw, clust, x, y, scaling):
    if clust.id < 0:
        h1 = getheight(clust.left) * 20
        h2 = getheight(clust.right) * 20
        top = y - (h1 + h2) / 2
        bottom = y + (h1 + h2) / 2
        line_length = clust.distance * scaling

        draw.line((x, top + h1/2, x, bottom - h2/2), fill=(255, 0, 0))
        draw.line((x, top + h1/2, x+line_length, top + h1/2), fill=(255, 0, 0))
        draw.line((x, bottom - h2/2, x+line_length, bottom-h2/2), fill=(255, 0, 0))

        drawnode(draw, clust.left, x+line_length, top+h1/2, scaling)
        drawnode(draw, clust.right, x+line_length, bottom-h2/2, scaling)
    else:
        draw.text((x+5, y-7), str(clust.id), (0, 0, 0))
