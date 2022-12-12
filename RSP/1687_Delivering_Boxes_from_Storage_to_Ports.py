def load_ship(boxes, maxb, maxw):
    load = []
    n, w, i = 0, 0, 0
    while(boxes and n<maxb and w<maxw):
        box = boxes.pop(0)
        load.append(box)
        n+=1
        w+=box[1]
        i+=1
    return load, boxes



def shippment(load):
    print(load)
    trips = 0
    while (load):
        port = load[0][0]
        print("port ", end="")
        print(port)
        trips+=1
        i=0
        # c = load[i][0]
        while (load[i][0]==port):
            load.pop(0)
            i+=1
    return trips+1



def boxDelivering(boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
    load = []
    trips = 0
    while(boxes):
        load, boxes = load_ship(boxes, maxBoxes, maxWeight)

        trips += shippment(load)

    return trips


if __name__ == "__main__":
    boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]]
    portsCount = 3
    maxBoxes = 3
    maxWeight = 6
    print(boxDelivering(boxes, portsCount, maxBoxes, maxWeight))