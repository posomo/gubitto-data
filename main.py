import requests
import json


def call_api(loop_cnt):
    url = "https://pcmap-api.place.naver.com/graphql"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "content-type": "application/json"
    }

    mydata = '''[
        {
            "operationName": "getVisitorReviewPhotosInVisitorReviewTab",
            "variables": {
                "businessId": "38521672",
                "businessType": "restaurant",
                "item": "0",
                "page": 1,
                "size": 20
            },
            "query": "query getVisitorReviewPhotosInVisitorReviewTab($businessId: String!, $businessType: String, $page: Int, $size: Int, $theme: String, $item: String) {  visitorReviews(    input: {businessId: $businessId, businessType: $businessType, page: $page, size: $size, theme: $theme, item: $item, isPhotoUsed: true, includeReceiptPhotos: false}  ) {    items {      id      rating      author {        id        nickname        from        imageUrl        objectId        url        borderImageUrl        __typename      }      body      thumbnail      media {        type        thumbnail        videoId        videoOriginSource        trailerUrl        __typename      }      tags      status      visited      originType      item {        name        code        options        __typename      }      businessName      isFollowing      visitCount      votedKeywords {        code        iconUrl        iconCode        displayName        __typename      }      __typename    }    starDistribution {      score      count      __typename    }    hideProductSelectBox    total    __typename  }}"
        },
        {
            "operationName": "getFollowingReviews",
            "variables": {
                "input": {
                    "businessId": "38521672"
                }
            },
            "query": "query getFollowingReviews($input: FollowingReviewsInput) {  followingReviews(input: $input) {    reviews {      id      apolloCacheId      rating      author {        id        nickname        from        imageUrl        objectId        url        review {          totalCount          imageCount          avgRating          __typename        }        theme {          totalCount          __typename        }        isFollowing        followerCount        followRequested        __typename      }      body      thumbnail      media {        type        thumbnail        thumbnailRatio        class        videoId        videoOriginSource        trailerUrl        __typename      }      tags      status      visitCount      viewCount      visited      created      reply {        editUrl        body        editedBy        created        date        replyTitle        __typename      }      originType      item {        name        code        options        __typename      }      businessName      votedKeywords {        code        iconCode        displayName        iconUrl        __typename      }      userIdno      loginIdno      reactionStat {        id        typeCount {          name          count          __typename        }        totalCount        __typename      }      hasViewerReacted {        id        reacted        __typename      }      nickname      __typename    }    reactionTypes {      name      emojiUrl      label      __typename    }    __typename  }}"
        },
        {
            "operationName": "getVisitorRatingReviews",
            "variables": {
                "input": {
                    "businessId": "38521672",
                    "businessType": "restaurant",
                    "item": "0",
                    "bookingBusinessId": null,
                    "page": 1,
                    "size": 10,
                    "includeContent": false,
                    "getUserStats": true,
                    "includeReceiptPhotos": true,
                    "cidList": [
                        "220036",
                        "220051",
                        "229294"
                    ],
                    "getReactions": true,
                    "getTrailer": true
                },
                "id": "38521672"
            },
            "query": "query getVisitorRatingReviews($input: VisitorReviewsInput) {  visitorReviews(input: $input) {    total    reactionTypes {      name      emojiUrl      label      __typename    }    items {      id      rating      author {        id        nickname        from        imageUrl        borderImageUrl        objectId        url        review {          totalCount          imageCount          avgRating          __typename        }        theme {          totalCount          __typename        }        isFollowing        followerCount        followRequested        __typename      }      visitCount      visited      originType      reply {        editUrl        body        editedBy        created        replyTitle        __typename      }      votedKeywords {        code        iconUrl        iconCode        displayName        __typename      }      businessName      status      userIdno      loginIdno      receiptInfoUrl      reactionStat {        id        typeCount {          name          count          __typename        }        totalCount        __typename      }      hasViewerReacted {        id        reacted        __typename      }      nickname      __typename    }    __typename  }}"
        },
        {
            "operationName": "getVisitorReviewThemeLists",
            "variables": {
                "input": {
                    "businessId": "38521672",
                    "page": 1,
                    "display": 3
                }
            },
            "query": "query getVisitorReviewThemeLists($input: ThemeListsInput) {  themeLists(input: $input) {    themeLists {      id      title      viewCount      itemCount      reviews {        businessName        reviewBody        imageUrl        __typename      }      authorNickname      authorImageUrl      isFollowing      themeListUrl      authorUrl      __typename    }    total    __typename  }}"
        },
        {
            "operationName": "getVisitorReviews",
            "variables": {
                "input": {
                    "businessId": "38521672",
                    "businessType": "restaurant",
                    "item": "0",
                    "bookingBusinessId": null,
                    "page": 1,
                    "size": 10,
                    "isPhotoUsed": false,
                    "includeContent": true,
                    "getUserStats": true,
                    "includeReceiptPhotos": true,
                    "cidList": [
                        "220036",
                        "220051",
                        "229294"
                    ],
                    "getReactions": true,
                    "getTrailer": true
                }
            },
            "query": "query getVisitorReviews($input: VisitorReviewsInput) {  visitorReviews(input: $input) {    items {      id      rating      author {        id        nickname        from        imageUrl        borderImageUrl        objectId        url        review {          totalCount          imageCount          avgRating          __typename        }        theme {          totalCount          __typename        }        isFollowing        followerCount        followRequested        __typename      }      body      thumbnail      media {        type        thumbnail        thumbnailRatio        class        videoId        videoOriginSource        trailerUrl        __typename      }      tags      status      visitCount      viewCount      visited      created      reply {        editUrl        body        editedBy        created        date        replyTitle        isReported        isSuspended        __typename      }      originType      item {        name        code        options        __typename      }      language      highlightOffsets      apolloCacheId      translatedText      businessName      showBookingItemName      bookingItemName      votedKeywords {        code        iconUrl        iconCode        displayName        __typename      }      userIdno      loginIdno      receiptInfoUrl      reactionStat {        id        typeCount {          name          count          __typename        }        totalCount        __typename      }      hasViewerReacted {        id        reacted        __typename      }      nickname      showPaymentInfo      __typename    }    starDistribution {      score      count      __typename    }    hideProductSelectBox    total    showRecommendationSort    itemReviewStats {      score      count      itemId      starDistribution {        score        count        __typename      }      __typename    }    reactionTypes {      name      emojiUrl      label      __typename    }    __typename  }}"
        },
        {
            "operationName": "getVisitorReviewStats",
            "variables": {
                "businessType": "restaurant",
                "id": "38521672",
                "itemId": "0"
            },
            "query": "query getVisitorReviewStats($id: String, $itemId: String, $businessType: String = \\\"place\\\") {  visitorReviewStats(    input: {businessId: $id, itemId: $itemId, businessType: $businessType}  ) {    id    name    apolloCacheId    review {      avgRating      totalCount      scores {        count        score        __typename      }      starDistribution {        count        score        __typename      }      imageReviewCount      authorCount      maxSingleReviewScoreCount      maxScoreWithMaxCount      __typename    }    analysis {      themes {        code        label        count        __typename      }      menus {        label        count        __typename      }      votedKeyword {        totalCount        reviewCount        userCount        details {          category          code          iconUrl          iconCode          displayName          count          previousRank          __typename        }        __typename      }      __typename    }    visitorReviewsTotal    ratingReviewsTotal    __typename  }}"
        }
    ]
    '''


    loads = json.loads(mydata)
    #print(loads)

    response = requests.post(url, headers=headers, data=mydata.encode())
    response_json = json.dumps(response.json())

    #print(json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False))

    print(f'call api[{loop_cnt}], text length {len(response.text)}, status code {response.status_code}')


for i in range(100):
    call_api(i)
