class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                if image[i][j]==1:
                    image[i][j]=0
                elif image[i][j]==0:
                    image[i][j]=1
        return image
