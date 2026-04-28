/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 15:07:58 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/10 17:10:07 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char		*tempd;
	const unsigned char	*temps;

	tempd = (unsigned char *)dest;
	temps = (const unsigned char *)src;
	while (n--)
		*tempd++ = *temps++;
	return (dest);
}
