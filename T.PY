def plotcolormap(df,title='ColorMap',patch=False):
    """
    This function plot the Lunar of the csv
    input:
    df:DataFrame to produce map
    title:title of the map
    patch:False/True for showing rectangle patch
    ouput:
    return:None
    """

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    if(patch==True):
    rect = patches.Rectangle((200,50),200,150, edgecolor='r', facecolor="none")
    ax.add_patch(rect)
    plt.imshow(df);


    