/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 18:35:38 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:43:00 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	i;
	size_t	dstlen;
	size_t	srclen;

	if (!dest || !src)
		return (0);
	i = 0;
	dstlen = 0;
	srclen = 0;
	while (*(dest + dstlen) && dstlen < size)
		++dstlen;
	while (*(src + srclen))
		++srclen;
	if (dstlen == size)
		return (dstlen + srclen);
	while (*(src + i) && dstlen + i < size - 1)
	{
		*(dest + dstlen + i) = *(src + i);
		++i;
	}
	*(dest + dstlen + i) = '\0';
	return (dstlen + srclen);
}
